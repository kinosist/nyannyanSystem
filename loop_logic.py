import time
import logging

try:
    import RPi.GPIO as GPIO
except ModuleNotFoundError:
    class MockGPIO:
        BCM = "BCM"
        IN = "IN"

        def __init__(self):
            self.start_time = time.time()

        def setmode(self, mode):
            logging.info(f"GPIO.setmode({mode})")

        def setup(self, pin, mode):
            logging.info(f"GPIO.setup({pin}, {mode})")

        def input(self, pin):
            elapsed = time.time() - self.start_time
            # 起動から30〜60秒の間はTrue、それ以外はFalse
            return 30 <= elapsed < 60

        def cleanup(self):
            logging.info("GPIO.cleanup()")

    GPIO = MockGPIO()

from utils.webhook_utils import notify


def watch_cat_feeder(sensor_pin: int, grace_time: int, webhook_url: str, channel: str) -> None:
    try:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(sensor_pin, GPIO.IN)
    except Exception as e:
        logging.critical(f"GPIOの初期化に失敗しました: {e}")
        return

    cat_present = False
    detection_start = None

    logging.info("[INFO] 猫検知システム 起動中…")

    try:
        while True:

            try:
                sensor_active = GPIO.input(sensor_pin)
            except Exception as e:
                logging.error(f"GPIOの入力取得に失敗: {e}")
                sensor_active= False

            if GPIO.input(sensor_pin):
                if not cat_present:
                    detection_start = time.time()
                    cat_present = True
                    logging.info("猫を検知しました。通知を送信します。")
                    try:
                        notify(webhook_url, channel, "🐱 猫が餌を食べに来ました！", "人感センサーが反応しました")
                    except Exception as e:
                        logging.error(f"Slackの通知に失敗しました(猫が来た): {e}")
            else:
                if cat_present and detection_start is not None:
                    duration = time.time() - detection_start
                    if duration >= grace_time:
                        logging.info(f"猫の食事終了を検知（所要時間:{int(duration)}秒。通知を送信します")
                        try:
                            notify(webhook_url, channel, f"✅ 猫が食事を終えました（所要時間：{int(duration)}秒）", "人感センサーの反応が切れました")
                        except Exception as e:
                            logging.error(f"Slackの通知に失敗しました(猫が帰った): {e}")
                        cat_present = False
                    else:
                        logging.info(f"猫は食事をしなかった:{int(duration)}秒。通知を送信しません")
                        cat_present = False
                else:
                    logging.debug("detection_start が未設定のまま duration を計算しようとしました。スキップします。")

            time.sleep(1)

    except KeyboardInterrupt:
        logging.warning("\n[INFO] システム停止")

    except Exception as e:
        logging.critical(f"予期しないエラーが発生しました: {e}")

    finally:
        try:
            GPIO.cleanup()
            logging.info("GPIOをクリーンアップしました。")
        except Exception as e:
            logging.error(f"GPIOのクリーンアップに失敗:{e}")
        
