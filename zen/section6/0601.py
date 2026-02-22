'''
zen.section6.0601 の Docstring
PP_06_01_リストを使ってみよう.ipynb
'''


# 文字列からリストを作る
'''
list 関数を使って、"a"、"b"、"c"、"d" の 4 つの値が入ったリストを作ってください。
'''
list("abcd")



# リストの連結
'''
それでは、 ["a", "b", "c", "d"] のリストを、変数 first4 に代入してください。
first (ファースト) は、最初の、という意味です。
また、 ["e", "f", "g"] のリストを、変数 next3 に代入してください。
next (ネクスト) は、次の、という意味です。
+ の演算子を使って、 first4 と next3 を連結してください。
'''
first4 = list("abcd")
next3 = list("efg")
result = first4 + next3
print(result)




# リストの繰り返し
'''
"赤巻紙"、"青巻紙"、"黄巻紙" の 3 つの要素が 3 回繰り返されるリストを作ってください。
'''
peper_list = ["赤巻紙", "青巻紙", "黄巻紙"] * 3
print(peper_list)




# in 演算子
'''
まず、12星座のリストを作ります。
星座 = [
    "おひつじ座", "おうし座", "ふたご座",
    "かに座", "しし座", "おとめ座",
    "てんびん座", "さそり座", "いて座",
    "やぎ座", "みずがめ座", "うお座"
    ]
in 演算子を使って、 "こぐま座" が12星座のリストに含まれるかどうか調べてください。
'''
constellation = ["おひつじ座", "おうし座", "ふたご座", "かに座", "しし座", "おとめ座", "てんびん座", "さそり座", "いて座", "やぎ座", "みずがめ座", "うお座"]
if "こぐま座" in constellation:
  print("yes")
else:
  print("no")



# not in
'''
not in 演算子を使って、星座のリストに "はくちょう座" が含まれていないことを確認してください。
'''
if "はくちょう座" not in constellation:
  print("no")
else:
  print("yes")



# for 文
'''
for 文を使って、英語月名リストの要素を 1 つずつ表示してください。
'''
month_list = [
    "January", "February", "March", "April",
    "May", "June", "July", "August",
    "September", "October", "November", "December"
    ]
for i in month_list:
  print(i)



# インデックスを用いた for 文
'''
for 文を使って、英語月名リストの要素を 1 つずつ順番に表示しましょう。
「1月の英語名はJanuaryです」「2月の英語名はFebruaryです」のように表示してください。
'''
for num in range(12):
    print(f"{num+1}月の英語名は{month_list[num]}です")



# enumerate
'''
enumerate を使って、英語月名リストの要素を 1 つずつ順番に表示しましょう。
「1月の英語名はJanuaryです」「2月の英語名はFebruaryです」のように表示してください。
'''
for num, name in enumerate(month_list):
    print(f"{num+1}月の英語名は{name}です")
