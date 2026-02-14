# ①引数と戻り値の両方がない関数（決まった仕事をさせたい時）
# print greet
def greet():
  print("こんにちは！")
greet()


# ②引数だけの関数（違うデータを渡して、処理を調整したい時）
# input user name
def user_name(name):
  print(f"{name}さん")
user_name(input("名前を入力してください。\n:"))



# ③戻り値だけの関数（処理に変化があり結果を知りたい場合）
# create kuji
import random

def omikuji():
  kuji = ["1", "2", "3"]
  return random.choice(kuji)
result = omikuji()
print(f"結果は{result}等")



# ④引数と戻り値のある関数（データを渡して計算する時や、実行結果を知りたい時）
# tax-calculation

def tax_calc(price):
  return int(price * 1.1)

price = int(input("値段を入力してください。\n:"))
tax = tax_calc(price)

print(f"税額は {tax} 円")
print(f" {price} 円の消費税込みの値段は {tax} 円です。")



