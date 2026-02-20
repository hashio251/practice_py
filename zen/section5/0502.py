'''
zen.section5.0502 の Docstring
PP_05_02_引数を受け取る関数.ipynb
'''



# 仮引数と実引数
'''
前回の授業で、誕生日のメッセージを表示する関数を作りました。
この関数を編集して、年齢を引数として受け取り、受け取った値を「〇歳」の部分に表示するようにしてください。
仮引数の名前は、 age などを使うとよいでしょう。
age (エイジ) は、年齢という意味です。
'''
def send_birthday_message(age):
  return f"{age}歳のお誕生日おめでとう！素敵な一年になりますように！"

age = int(input("何歳になりましたか？"))
birthday_message = send_birthday_message(age)

print(birthday_message)



# 関数の説明を書く
'''
ドックストリングを使って、誕生日のメッセージを表示する関数に説明を加えてください。
'''
def send_birthday_message(age):
  return f"{age}歳のお誕生日おめでとう！素敵な一年になりますように！"

age = int(input("何歳になりましたか？"))
'''
ここで誕生日のメッセージを表示させる関数を呼び出し変数に代入
'''
birthday_message = send_birthday_message(age)

print(birthday_message)



# 引数の説明を書く
'''
誕生日のメッセージを表示する関数のドックストリングに、引数の説明を加えてください。
'''
def send_birthday_message(age):
  return f"{age}歳のお誕生日おめでとう！素敵な一年になりますように！"

'''
intの型を指定してユーザーからの入力を受け取ってageという変数に代入
'''
age = int(input("何歳になりましたか？"))
'''
ここで誕生日のメッセージを表示させる関数を呼び出し変数に代入
'''
birthday_message = send_birthday_message(age)

print(birthday_message)
