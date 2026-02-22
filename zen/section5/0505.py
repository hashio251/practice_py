'''
zen.section5.0505 の Docstring
PP_05_05_戻り値を返す関数.ipynb
'''


# 関数を呼び出す
'''
摂氏から華氏へ 関数を使って、摂氏100度を華氏に変換してください。
そして、「摂氏100度は華氏〇度です」と表示してください。
〇には、具体的な値を入れてください。
'''
def celsius_to_fahrenheit(celsius):
    fahrenheit = celsius * 1.8 + 32
    return fahrenheit

c = 100
f = celsius_to_fahrenheit(c)

print(f"摂氏{c}度は華氏{f}度です。")




# 式を返す
'''
華氏温度から摂氏温度へ変換するには、以下の公式を使います。
摂氏温度=(華氏温度−32)×59
華氏温度を引数として受け取り、摂氏温度に変換して戻り値として返す関数を定義してください。
この関数に 32 を渡すと、 0 が返ってくることを確認してください。
この関数に 212 を渡すと、 100 が返ってくることを確認してください。
'''
def fahrenheit_to_celsius(fahrenheit):
    celsius = (fahrenheit - 32) * 5 / 9
    return celsius

f = 32
f = 212
c = fahrenheit_to_celsius(f)

print(f"華氏{f}度は摂氏{c}度です。")



# 関数に別の名前を付ける
'''
華氏から摂氏へ 関数に f2c という名前を付けてください。
そして、f2c を使って、華氏100 ∘ F を摂氏に変換してください。
華氏100 ∘ F は、高熱とみなされる体温です。
'''
f = 100
f2c = fahrenheit_to_celsius
c = f2c(f)

print(f"華氏{f}度は摂氏{c}度です。")



# return
'''
ナルシスト関数を以下のように編集してください。
最初に input 関数を使って、「ナルシスト関数の独白を聞きますか？」と聞いてください。
独白とは、相手なしにひとりでセリフを言うことです。
もしユーザーが「いいえ」と答えたら、 return 文を使って関数を終わらせてください。
そうでなければ、セリフを表示してください。
'''
def love_self():
    u_ans = input("ナルシスト関数の独白を聞きますか？")
    if u_ans == "いいえ":
        return
    print("僕は、すごい。")
    print("僕は、賢く、そして美しい。")
    print("僕は、世界一の関数なんだ。")

love_self()
