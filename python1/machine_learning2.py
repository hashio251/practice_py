from sklearn import datasets
import matplotlib.pyplot as plt

digits = datasets.load_digits()

# imagesが存在しない--> reshapeする
try:
    images = digits.images
except AttributeError:
    images = digits.data.reshape(-1, 8, 8)

for i in range(50):
    plt.subplot(5, 10, i +1)
    plt.axis("off")
    plt.title(digits.target[i])
    plt.imshow(images[i], cmap="gray")
plt.show()
