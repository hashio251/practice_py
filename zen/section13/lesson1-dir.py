import os

with open("example.txt", "w", encoding="utf-8") as my_file:
    my_file.write("書き込みたい文字列")
os.getcwd()
os.chdir("./section13")
with open("count.txt", "w", encoding="utf-8") as f:
    f.write("one two three")

os.getcwd()
os.chdir("..")
os.getcwd()