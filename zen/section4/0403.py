'''
zen.section4.0403 の Docstring
rangeを使った繰り返し
'''


# 単調な繰り返し
'''
for 文と range 関数を使って、「赤巻紙青巻紙黄巻紙」と10 回表示するコードを書いてください。
'''
color_list = ["赤", "青", "黄"]
for _ in range(10):
  i = 0
  while i < len(color_list):
    print(f"{color_list[i]}巻紙", end="")
    i += 1
  print()



# インクリメント
'''
for 文を使って、11 から 99 までの数字を表示するコードを書いてください。
'''
for i in range(11, 100):
  print(i, end=" ")



# 同一処理の繰り返し
'''
range 関数を使って、「赤巻紙青巻紙黄巻紙」と 7 回表示するコードを書いてください。
'''
color_list = ["赤", "青", "黄"]
for _ in range(7):
  i = 0
  while i < len(color_list):
    print(f"{color_list[i]}巻紙", end="")
    i += 1
  print()



# 規則的な繰り返し
'''
冬季オリンピックは、夏季オリンピックの間の年に開催されます。
2002年、2006年、2010年のように、やはり 4 年ごとに開催されます。
2002年～2042年の冬季オリンピックの開催年を表示するコードを書いてください。
'''
for i in range(2002, 2043, 4):
  print(i)



# デクリメント
'''
for 文と range を使って、5日前、 4日前、3日前、2日前、1日前、と表示するコードを書いてください。
'''
for i in range(5, 0, -1):
  print(f"{i}日前")