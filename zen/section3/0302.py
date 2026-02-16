'''
zen.section3.0302 の Docstring
elif文
演習問題
'''

'''
次のコードセルの 2 行目以降に、変数 季節 の値が "春" のときは "Spring"、 "夏" の時は "Summer"、それ以外のときは "Not spring, not summer" と表示するコードを書いてください。
'''
# if else
season = "春"
if season == "春":
  print("Spring")
else:
  if season == "夏":
    print("Summer")
  else:
    print("Not spring, not summer")




# 多重ネスティング
'''
先ほどのコードを編集して、変数 季節 の値が "春" のときは "Spring"、 "夏" のときは "Summer"、 "秋" のときは "Fall"、それ以外のときは "Other season" と表示されるようにしてください。
season (シーズン) は、季節という意味です。
'''
season = "春"
if season == "春":
  print("Spring")
else:
  if season == "夏":
    print("Summer")
  else:
    if season == "秋":
      print("Fall")
    else:
      print("Other season")




# elif
'''
先ほど書いた、季節の名前を英語で表示するコードを、 elif 文を使って書き直してください。
'''
season = "春"
if season == "春":
  print("Spring")
elif season == "夏":
  print("Summer")
elif season == "秋":
  print("Fall")
else:
  print("Other season")


'''
柔道女子の階級は、48kg級・52kg級・57kg級・63kg級・70kg級・78kg級・78kg超級の 7 階級です。
体重にもとづいて選手を階級に分けるコードを、以下のコードセルの 2 行目以降に書いてください。
'''
weight = 60
if weight <= 48:
  print("48kg class")
elif weight <= 52:
  print("52kg class")
elif weight <= 57:
  print("57kg class")
elif weight <= 63:
  print("63kg class")
elif weight <= 70:
  print("70kg class")
elif weight <= 78:
  print("78kg class")
else:
  print("83kg over class")
