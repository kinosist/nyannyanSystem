from pathlib import Path
from loop_logic import watch_cat_feeder
from utils.json_utils import load_json
import logging
import time

# 安全なパス解決（スクリプトのある場所を基点とする）
BASE_DIR = Path(__file__).resolve().parent
CONFIG_PATH = (BASE_DIR / "data/config.json").resolve()
config = load_json(str(CONFIG_PATH))

base_log_level = getattr(logging, config.get("log_level", "INFO").upper(), logging.INFO)
base_formatter = logging.Formatter("%(asctime)s [%(levelname)s] [%(filename)s:%(lineno)d %(funcName)s] %(message)s")

stream_handler = logging.StreamHandler()
stream_handler.setLevel(base_log_level)
stream_handler.setFormatter(base_formatter)

file_handler = logging.FileHandler(
    config.get("log_file", "system.log")
)
file_handler.setLevel(base_log_level)
file_handler.setFormatter(base_formatter)

def main():

    logging.basicConfig(
        level=logging.NOTSET,
        handlers=[stream_handler, file_handler],
        datefmt= "%Y-%m-%d %H:%M:%S",
    )

    try:
        watch_cat_feeder(
        sensor_pin=config["sensor_gpio_pin"],
        grace_time=config["detection_grace_time_sec"],
        webhook_url=config["slack_webhook_url"],
        channel=config["slack_webhook_channel"]
        )
    except Exception as e:
        logging.critical(f"センサー監視中にエラーが発生しました: {e}")
        time.sleep(10)




if __name__ == "__main__":
    main()
