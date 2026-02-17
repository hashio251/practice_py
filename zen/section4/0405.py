'''
zen.section4.0405 の Docstring
break文
'''


# for ループから抜け出す
'''
以下のコードセルの 1 行目に、体重を聞いて、答えを浮動小数型に変換してから変数 weight に代入するコードを書いてください。
そして、 2 行目以降に、体重にもとづいて女子選手を階級に分けるコードを書いてください。
柔道女子の階級は、48kg級・52kg級・57kg級・63kg級・70kg級・78kg級・78kg超級の 7 階級です。
'''
weight = float(input("あなたの体重は何キロですか？"))
for i in [48, 52, 57, 63, 70, 78]:
    if weight <= i:
        print(f"{i}kg級")
        break
if weight > 78:
    print("78kg超級")



# input を使った while 文
'''
ユーザーからの返事が「いいえ」の間、「もうやめますか？」と聞き続けるコードを書いてください。
'''
while True:
    user_answer = input("もうやめますか？")
    if user_answer != "いいえ":
        break
print("終了します。")


# while ループから抜け出す
'''
while 文を使って、ユーザーからの入力を求め続けるプログラムを作ってください。
ただし、ユーザーからの入力が特定の条件を満たしたら、ループから抜け出すようにしてください。
'''
while True:
    answer = input("お腹が空きましたか？")
    if answer == "はい":
        break
print("ご飯にしましょう。")

