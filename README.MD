# NASA 天文学写真日報（APOD）ビューア

このプロジェクトは、NASA APIを使用して天文学写真日報（Astronomy Picture of the Day, APOD）を表示するシンプルなWebアプリケーションです。Python、Flask、Dockerを使用して構築されています。

## 機能

- その日の天文学写真日報を表示
- 画像のタイトル、日付、説明、著作権情報を表示
- デスクトップとモバイルの両方に対応したレスポンシブデザイン

## 前提条件

始める前に、以下の要件を満たしていることを確認してください：

- [Docker](https://www.docker.com/get-started) と [Docker Compose](https://docs.docker.com/compose/install/) がインストールされていること
- [NASA API](https://api.nasa.gov/) から取得したAPIキーがあること

## セットアップ

1. リポジトリをクローンします：
   ```
   git clone https://github.com/あなたのユーザー名/nasa-apod-viewer.git
   cd nasa-apod-viewer
   ```

2. ルートディレクトリに `.env` ファイルを作成し、NASA APIキーを追加します：
　　APIキーは以下のリンクから取得することができます。
　　https://api.nasa.gov/

   ```
   NASA_API_KEY=あなたのAPIキーをここに
   ```

3. Dockerコンテナをビルドして実行します：
   ```
   docker-compose up --build
   ```

## 使用方法

アプリケーションが起動したら、Webブラウザを開いて以下のURLにアクセスしてください：

```
http://localhost:5000/apod
```

これにより、その日の天文学写真日報と詳細情報が表示されます。

## プロジェクト構造

```
nasa-apod-viewer/
│
├── app/
│   └── main.py
├── .dockerignore
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── requirements.txt
└── README.md
```

## 貢献

このプロジェクトへの貢献を歓迎します。リポジトリをフォークし、変更内容をプルリクエストとして提出してください。

## ライセンス

このプロジェクトはMITライセンスの下で公開されています。詳細は [LICENSE](LICENSE) ファイルをご覧ください。

## 謝辞

- APOD APIを提供しているNASA
- 優れたWebフレームワークを提供しているFlaskチーム
- デプロイメントプロセスを簡素化してくれるDocker