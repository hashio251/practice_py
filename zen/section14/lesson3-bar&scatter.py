import matplotlib.pyplot as plt

# font
plt.rcParams["font.family"] = "Hiragino Sans"

# add data
cities = ["札幌", "仙台", "東京", "新潟", "静岡", "京都", "大阪", "岡山", "広島", "福岡", "鹿児島", "那覇"]
low = [-6.2, -1.1, 2.1, -0.1, 2.9, 1.6, 3.2, 0.5, 2.4, 4.4, 5.8, 15.1]
high = [26.4, 28.2, 31.3, 30.8, 31.3, 33.7, 33.7, 33.3, 32.8, 32.5, 32.7, 31.8]

# draw scatter
plt.scatter(low, high)
plt.savefig("./images/最低気温と最高気温の関係.png")
plt.show()

# add label data
plt.xlabel("2月の最低気温")
plt.ylabel("8月の最高気温")
plt.scatter(low, high)
plt.text(-6.2, 26.4, "札幌")
plt.savefig(".|images|最低気温と最高気温の関係.png")
plt.show()

# add city
plt.xlabel("2月の最低気温")
plt.ylabel("8月の最高気温")
plt.scatter(low, high)
for i in range(len(cities)):
    plt.text(low[i], high[i], cities[i])
plt.savefig(".|images|最低気温と最高気温の関係.png")
plt.show()

# bar graph
nobel_prize = dict(物理学=12, 化学=8, 生理学医学=5, 文学=2, 平和=1, 経済学=0)

# draw bar
plt.title("日本人のノーベル賞受賞者数")
plt.bar(nobel_prize.keys(), nobel_prize.values())
plt.savefig("./images/ノーベル賞の受賞者数.png")
plt.show()