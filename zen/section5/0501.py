'''
zen.section5.0501 の Docstring
PP_05_01_関数を作ってみよう.ipynb
'''

# 関数名の付け方
'''
send_birthday_message という名前の関数を定義してください。
send (センド) は送る、 birthday (バースデー) は誕生日、 message (メッセージ) はメッセージという意味です。
この関数が呼び出されたとき、以下のメッセージが表示されるようにしましょう。
〇歳のお誕生日おめでとう。
素敵な1年になりますように！
'''
def send_birthday_message(age):
  return f"{age}歳のお誕生日おめでとう！素敵な一年になりますように！"

age = input("何歳になりましたか？")
birthday_message = send_birthday_message(age)

print(birthday_message)