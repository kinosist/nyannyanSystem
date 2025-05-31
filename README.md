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

---

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

1. 取得したwebhook_urlを.envのSLACK_WEBHOOK_URLに追加
2. botを追加したチャンネル名を.envのSLACK_WEBHOOK_CHANNELに追加

---

## 🔗 参考

- [Zenn 記事](https://zenn.dev/hotaka_noda/articles/4a6f0ccee73a18)
- [Slack API 公式](https://api.slack.com/messaging/webhooks)

---

## 赤外線センサーのセットアップ

一般的な3ピンの赤外線センサーをRaspberry Piに接続する手順を説明します。

### ✅ 準備するもの

  * 赤外線センサーモジュール (HC-SR501など)
  * Raspberry Pi (任意のモデル)
  * ジャンパーワイヤー (メス-メス または メス-オス、センサーのピンタイプによる)

### ✅ ピン配置の確認

赤外線センサーには通常、以下の3つのピンがあります。中央のPINがOUTのことが多いです。

  * **VCC**: 電源ピン (通常 5V または 3.3V)
  * **GND**: グランドピン
  * **OUT** (または **SIGNAL**): センサーの検知信号を出力するピン

### ✅ Raspberry Piとの接続

1.  **VCCピンの接続**:
      * 赤外線センサーの **VCC** ピンを、Raspberry Pi の **5V** ピン (ピン番号 2 または 4) に接続します。
      * センサーが3.3V駆動の場合は、Raspberry Pi の **3.3V** ピン (ピン番号 1 または 17) に接続します。
2.  **GNDピンの接続**:
      * 赤外線センサーの **GND** ピンを、Raspberry Pi の **GND** ピン (例: ピン番号 6, 9, 14, 20, 25, 30, 34, 39) のいずれかに接続します。
3.  **OUTピンの接続**:
      * 赤外線センサーの **OUT** ピンを、Raspberry Pi の任意の **GPIOピン** (例: GPIO17 / ピン番号 11) に接続します。このピンでセンサーの信号を読み取ります。

> ⚠️ **注意点**
>
>   * 接続する前に、Raspberry Piの電源がオフになっていることを確認してください。
>   * センサーによっては、VCCとGNDの配置が異なる場合があります。必ずセンサーの仕様書や基板の表記を確認してください。誤った接続はセンサーやRaspberry Piの故障の原因となります。

---

## 🔗 参考

- [Hatena Blog 記事](https://aquarius-train.hatenablog.com/entry/RaspberryPi_3B%2B%E3%81%A7%E4%BA%BA%E6%84%9F%E3%82%BB%E3%83%B3%E3%82%B5%E3%83%BC%E3%81%AE%E5%8B%95%E4%BD%9C%E7%A2%BA%E8%AA%8D)