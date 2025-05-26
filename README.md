# プロジェクト名

にゃんにゃん食事検知システム

## 📦 概要

Raspberry piと赤外線センサーで猫が餌を食べに来たか検知してSlackに送るシステムです：

## 🛠️ インストール

以下の手順でRaspberry pi環境にセットアップできます。

```bash
# リポジトリをクローン
git clone https://github.com/kinosist/nyannyanSystem.git nekosyokukanti-kun
cd nekosyokukanti-kun
```

```bash
# 依存関係をインストール
pip install -r requirements.txt
```

```bash
# アプリを起動
python main.py
```

## SlackのWebhook URLを取得する方法

PythonなどからSlackへ通知を送るには、**Webhook URL**を取得する必要があります。以下の手順に従ってSlackのIncoming Webhookを設定し、URLを取得してください。

### ✅ 手順

#### 1. Slack Appの作成

1. [Slack API: Your Apps](https://api.slack.com/apps) にアクセスします。
2. 「Create New App」ボタンをクリックします。
3. 「From scratch」を選択し、以下の情報を入力します：
   - **App Name**: 任意（例：`nekosyokukanti-kun`）
   - **Workspace**: 使用するSlackワークスペースを選択

#### 2. Incoming Webhooksを有効化

1. アプリ作成後の設定画面で、左メニューの「**Incoming Webhooks**」を選択
2. 「**Activate Incoming Webhooks**」を `On` にします

#### 3. Webhook URLの作成

1. 下の「**Add New Webhook to Workspace**」ボタンをクリック
2. 通知を送信したい**チャンネルを選択**
3. 「**許可する**」をクリック
4. Webhook URL が生成されるのでコピー

> 例:
> ```
> https://hooks.slack.com/services/T00000000/B00000000/XXXXXXXXXXXXXXXXXXXXXXXX
> ```

#### 4. WebHookの設定方法

1. 取得したwebhook_urlをdata/config.jsonのslack_webhook_urlに追加
2. botを追加したチャンネル名をdata/config.jsonのslack_webhook_channelに追加

---

## 🔗 参考

- [Zenn 記事](https://zenn.dev/hotaka_noda/articles/4a6f0ccee73a18)
- [Slack API 公式](https://api.slack.com/messaging/webhooks)

