# 動作確認
Ubuntu 20.04.4 LTS
python 3.9.7

# アプリ構成

```bash
image_app/

    |-app.py

    |-model.py
        |-Model : 画像データの管理や画像処理を担当するクラス

    |-view.py
        |-View : アプリのUIを管理するクラス

        |-MainFrame : メインフレームのUIを管理するクラス

            |-CanvasFrame : キャンバスフレームのUIを管理するクラス
                |-BeforeCanvasWidget : 画像処理前の画像を表示するキャンバスUIを管理するクラス
                |-AfterCanvasWidget : 画像処理後の画像を表示するキャンバスUIを管理するクラス

            |-ButtonFrame : ボタンフレームのUIを管理するクラス
                |-FileReadButtonWidget : 画像ファイル読み込みボタンUIを管理するクラス
                |-InvertButtonWidget : ネガポジ処理ボタンUIを管理するクラス
                |-FlipButtonWidget : 左右反転処理ボタンUIを管理するクラス

    |-controller.py
        |-Controller : ModelとViewの接続を管理するクラス
```

# 準備

## 仮想環境の作成

```bash
$ cd [project dir]
$ python3 -m venv [newenvname]
```

## 仮想環境に入る

### Windowsコマンドプロンプトの場合

```bash
$ .\Scripts\activate
```

### Ubuntuの場合
```bash
$ source ./[newenvname]/bin/activate
```

## 必要なパッケージのインストール

```bash
$ pip install -r requirements.txt
```

# 実行

```bash
$ python app.py
```

