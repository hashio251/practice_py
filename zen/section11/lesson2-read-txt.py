#️　テキストファイルの読み込み

my_file = open("profile.txt", "r", encoding="utf-8")
my_file.read()
my_file.close()
my_file.readline()
my_file.close()

with open("profile.txt", "r", encoding="utf-8") as myfile:
  my_file.read()



#️　テキストファイルの読み込み+a

my_file = open("profile.txt", "a+", encoding="utf-8")
my_file.seek(0)
my_file.read()
my_file.write("チャームポイント：髪の毛")
my_file.close()