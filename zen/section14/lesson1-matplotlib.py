import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4, 5]
y = [0, 1, 4, 9, 16, 25]

# 折れ線グラフ
plt.plot(x, y)
plt.show()

# 散布図
plt.scatter(x, y)
plt.show()

# 棒グラフ
plt.bar(x, y)
plt.show()