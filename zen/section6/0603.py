'''
zen.section6.0603 の Docstring
PP_06_03_リストの演算.ipynb
'''

import random


# len 関数を使って、 countries リストの長さを調べてください。
cities = ["Sydney", "Athens", "Beijing", "London", "Rio de Janeiro", "Tokyo"]
countries = ["Australia", "Greece", "China", "United Kingdom", "Brazil", "Japan"]

print(len(countries))



# sum 関数を使って、銀メダルの総獲得数を計算してください。
gold_medals = [5, 16, 9, 7, 12, 27]
silver_medals = [8 ,9, 6, 14, 8, 14]
bronze_medals = [5, 12, 10, 17, 21, 17]

print(sum(silver_medals))


# 銀メダルの獲得数の最小値を求めてください。
print(min(silver_medals))



# 銀メダルの獲得数の最大値を求めてください。
print(max(silver_medals))



# iroha リストの要素を、あいうえお順に並べ替えてください。
iroha = ["i", "ro", "ha", "ni", "ho", "he", "to"]
print(sorted(iroha))



# 今度は、あいうえお順の逆に並べ替えてください。
print(sorted(iroha, reverse=True))



# choice 関数を使って、 omikuji リストの要素をランダムに 1 つ取り出してください。
omikuji = ["1", "2", "3", "4", "5", "6", "7"]
print(random.choice(omikuji))



# shuffle 関数を使って、 players リストの要素をランダムに並べ替えてください。
random.shuffle(omikuji)
print(omikuji)