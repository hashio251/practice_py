import matplotlib.pyplot as plt

# add data
years = [1950, 1960, 1970, 1980, 1990, 2000, 2010, 2020]
num_countries = [60, 99, 127, 154, 159, 189, 192, 193]

plt.plot(years, num_countries)
plt.show()

# marker
plt.plot(years, num_countries, marker="*")
plt.show()

# big marker
plt.plot(years, num_countries, marker="*", markersize=20)
plt.show()

# save graph
import os
os.mkdir("images")

# draw graph
plt.plot(years, num_countries, marker="*", markersize=20)

# rename save
plt.savefig("./images/国際連合加盟国数の推移.png")

# add title
plt.title("国際連合加盟国数")
plt.plot(years, num_countries, marker="*", markersize=20)
plt.savefig("./images/国際連合加盟国数の推移.png")
plt.show()

# setting languege in japanese
plt.rcParams["font.family"] = "Hiragino Sans"