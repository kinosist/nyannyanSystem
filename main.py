import os
from pathlib import Path
from loop_logic import watch_cat_feeder
# from utils.json_utils import load_json
import logging
import time
from dotenv import load_dotenv

# 安全なパス解決（スクリプトのある場所を基点とする）
BASE_DIR = Path(__file__).resolve().parent
# .env ファイルをロード
BASE_DIR = Path(__file__).resolve().parent
load_dotenv(BASE_DIR / ".env") # .envファイルのパスを指定

# CONFIG_PATH = (BASE_DIR / "data/config.json").resolve()
# config = load_json(str(CONFIG_PATH))

# ログレベルの設定 (環境変数が未設定の場合は INFO をデフォルトとする)
log_level_str = os.getenv("LOG_LEVEL", "INFO").upper()
base_log_level = getattr(logging, log_level_str, logging.INFO)
base_formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d %(funcName)s] %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setLevel(base_log_level)
stream_handler.setFormatter(base_formatter)

# ログファイル名の設定 (環境変数が未設定の場合は system.log をデフォルトとする)
log_file_name = os.getenv("LOG_FILE", "system.log")
file_handler = logging.FileHandler(log_file_name)
file_handler.setLevel(base_log_level)
file_handler.setFormatter(base_formatter)

def main():

    logging.basicConfig(
        level=logging.NOTSET,
        handlers=[stream_handler, file_handler],
        datefmt= "%Y-%m-%d %H:%M:%S",
    )

    try:
        # 環境変数から直接値を取得し、必要な場合は型変換を行う
        sensor_pin = int(os.getenv("SENSOR_GPIO_PIN"))
        grace_time = int(os.getenv("DETECTION_GRACE_TIME_SEC", 10))
        webhook_url = os.getenv("SLACK_WEBHOOK_URL")
        channel = os.getenv("SLACK_WEBHOOK_CHANNEL")

        if not all([sensor_pin, webhook_url, channel]):
            logging.critical("必要な環境変数が設定されていません。プログラムを終了します。")
            exit()

        watch_cat_feeder(
            sensor_pin=sensor_pin,
            grace_time=grace_time,
            webhook_url=webhook_url,
            channel=channel
        )
    except ValueError as e:
        logging.critical(f"環境変数の型変換に失敗しました: {e}")
    except Exception as e:
        logging.critical(f"センサー監視中にエラーが発生しました: {e}")
        time.sleep(10)




if __name__ == "__main__":
    main()
