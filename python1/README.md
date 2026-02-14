# python1年生

『**Python1年生 第2版 体験してわかる！会話でまなべる！プログラミングのしくみ**』（翔泳社）を参考に、学習しながら改変し書いたコードをまとめたディレクトリです。

## ディレクトリ構成

```
python1/
├── app1.py              # おみくじ GUI アプリ（tkinter）
├── app2.py              # 画像プレビュー GUI アプリ（tkinter + PIL）
├── bmi.py               # BMI 計算プログラム
├── create_def.py        # 関数の作り方（引数・戻り値のパターン）
├── draw_turtle.py       # turtle モジュールで図形を描画
├── import_module.py     # モジュールのインポート練習（カレンダー表示）
├── kuku.py              # 九九の表を出力
├── machine_learning.py  # 手書き数字データの読み込み
├── machine_learning1.py # 手書き数字画像の表示
├── machine_learning2.py # 手書き数字画像の一覧表示
├── omikuji.py           # おみくじプログラム
└── README.md
```

## 各ファイルの説明

| ファイル | 内容 |
|---|---|
| `app1.py` | tkinter でおみくじの GUI アプリを作成（`omikuji.py` をインポート） |
| `app2.py` | tkinter + PIL で画像を開いてモザイク風に表示する GUI アプリ |
| `bmi.py` | 身長・体重を入力して BMI を計算し、判定結果を表示する |
| `create_def.py` | 引数・戻り値の有無による 4 パターンの関数定義を学ぶ |
| `draw_turtle.py` | turtle グラフィックスで四角形・星・花を描く |
| `import_module.py` | `calendar` / `time` モジュールを使ってカレンダーを表示する |
| `kuku.py` | 二重ループで九九の表を出力する |
| `machine_learning.py` | scikit-learn の手書き数字データセットを読み込んで確認する |
| `machine_learning1.py` | matplotlib で手書き数字画像を 1 枚表示する |
| `machine_learning2.py` | matplotlib で手書き数字画像を 50 枚一覧表示する |
| `omikuji.py` | ランダムにおみくじの結果を表示する |

## 実行方法

Python 3 が必要です。

```bash
python bmi.py
python omikuji.py
python draw_turtle.py
```

> `draw_turtle.py` は GUI ウィンドウが開きます。

## 注意事項

- このコードは個人の学習目的で作成したものです。
- 書籍の文章・図版をそのまま転載しているものではありません。