import sklearn.datasets
import sklearn.svm
from PIL import Image, ImageFilter, ImageOps
import numpy as np
import glob

# 画像ファイル8×8の数値データ
def image_to_data(filename):
    # 画像読み込み--> グレースケール--> 8×8 に縮小
    img = Image.open(filename).convert("L")
    img = img.filter(ImageFilter.MedianFilter(size=3))
    img = img.point(lambda x: 0 if x < 128 else 255, 'L')
    bbox = img.getbbox()
    img = img.crop(bbox)
    img = ImageOps.pad(img, (8, 8), color=255)
    img = img.resize((8, 8), Image.Resampling.LANCZOS)

    # NumPyに変換（0-255）
    np_img = np.asarray(img, dtype=float)
    # digitsデータセットと同じ0-16に変換
    np_img = 16 - np.floor(17 * np_img / 256)

    # 1次元ベクトルに変換（64次元）
    return np_img.flatten()

# 数字を予測する
def predict_digit(data):
    # digitsデータセット読み込
    digits = sklearn.datasets.load_digits()

    # SVMモデルを作成して学習
    clf = sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target)

    # 予測結果を返す
    return clf.predict([data])[0]

# PNG画像を全部取得
image_files = sorted(glob.glob("images/*.png"))

for filename in image_files:
    # 予測
    data = image_to_data(filename)
    result = predict_digit(data)
    print(f"{filename} → 予測 = {result}")