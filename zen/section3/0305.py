'''
zen.section3.0304 の Docstring
for文
演習問題
'''


# 同一処理の繰り返し
'''
for 文を使って、「赤巻紙青巻紙黄巻紙」と 3 回表示するコードを書いてください。
'''
for i in range(3):
  print("赤巻紙青巻紙黄巻紙")



# 数を変えながらの繰り返し
'''
柔道女子の階級は、48kg級・52kg級・57kg級・63kg級・70kg級・78kg級・78kg超級の 7 階級です。
これらの階級を表示するコードを、次のコードセルの 2 行目以降に書いてください。
'''
w_class = [48, 52, 57, 63, 70, 78]
print("柔道女子の階級は、", end="")
for i in w_class:
  print(f"{i}kg級・", end="")
print(f"{w_class[-1]}kg超級の７階級です。")



# 文字列を変えながらの繰り返し
'''
for ループを使って、「赤巻紙」、「青巻紙」、「黄巻紙」と順に表示するコードを書いてください。
'''
peper_color = ["赤", "青", "黄"]
for i in peper_color:
  print(f"{i}巻紙")



# 二重ループ
'''
二重ループを使って、「赤巻紙」、「青巻紙」、「黄巻紙」と 3 回表示するコードを書いてください。
'''
peper_color = ["赤", "青", "黄"]
for _ in range(3):
  for color in peper_color:
    print(f"{color}巻紙")



# 改行をコントロールする
'''
以下のコードを編集して、 1 回ごとに改行しながら、「赤巻紙青巻紙黄巻紙」と 3 回表示されるようにしてください。
'''
peper_color = ["赤", "青", "黄"]
for _ in range(3):
  for color in peper_color:
    print(f"{color}巻紙", end="")
    print()