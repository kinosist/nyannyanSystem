import time
import requests
from typing import Any, Dict


def send_webhook_json(webhook_url: str, payload: Dict[str, Any]) -> None:
    """
    指定されたWebhook URLに対してJSONペイロードをPOST送信する。

    副作用: 外部のURLにHTTPリクエストを送信するネットワーク操作を行う。

    Args:
        webhook_url (str): 送信先のWebhook URL。
        payload (dict[str, Any]): 送信するJSONデータ。
    """
    try:
        response = requests.post(webhook_url, json=payload)
        response.raise_for_status()
    except requests.RequestException as e:
        print(f"[ERROR] Webhook送信に失敗しました: {e}")


def build_payload(channel: str, text: str, attachment_text: str) -> dict:
    """
    Slack用のWebhookペイロードを構築する純粋関数。

    Args:
        channel (str): 通知を送るSlackチャンネル。
        text (str): メインのメッセージ本文。
        attachment_text (str): アタッチメント内のテキスト。

    Returns:
        dict: Slackに送信するJSONペイロード。
    """
    return {
        "username": "CatBot",
        "icon_emoji": ":cat:",
        "channel": channel,
        "text": text,
        "attachments": [
            {
                "color": "#36a64f",
                "title": "監視カメラ通知",
                "text": attachment_text,
                "footer": "自動通知システム",
                "ts": time.time()
            }
        ]
    }


def notify(webhook_url: str, channel: str, text: str, attachment_text: str) -> None:
    payload = build_payload(channel, text, attachment_text)
    send_webhook_json(webhook_url, payload)
    print(f"[INFO] 通知送信: {text}")
