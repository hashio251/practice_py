#️　テキストファイルの書き込み

my_file = open("profile.txt", "w", encoding="utf-8")
my_file.write("名前：あすたりす\n")
my_file.close()

my_file = open("profile.txt", "a", encoding="utf-8")
my_file.write("好きな食べ物：ラーメン\n")
my_file.close()

with open("profile.txt", "a", encoding="utf-8") as my_file:
    my_file.write("趣味：ラーメン巡り\n")

with open("profile.txt", "a", encoding="utf-8") as my_file:
    my_file.write("趣味：和菓子作り\n")