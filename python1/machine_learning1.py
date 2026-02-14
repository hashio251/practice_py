from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()

# imagesが存在しない--> reshapeする
try:
    images = digits.images
except AttributeError:
    images = digits.data.reshape(-1, 8, 8)

plt.imshow(images[0], cmap="gray")
plt.show()
