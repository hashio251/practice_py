from sklearn import datasets

digits = datasets.load_digits()

# imagesが存在しない--> reshapeする
try:
    images = digits.images
except AttributeError:
    images = digits.data.reshape(-1, 8, 8)

print("データの個数=", len(images))
print("画像データ=", images[0])
print("何の数字であるかどうか=", digits.target[0])
