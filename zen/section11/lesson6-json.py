# json

asutarisu = {"好きな食べ物": "スイカ",
             "趣味": "和菓子作り",
             "チャームポイント": "しっぽ"}

with open("asutarisu.txt", "w", encoding="utf-8") as file_obj:
  file_obj.write(str(asutarisu))

with open("asutarisu.txt", "r", encoding="utf-8") as file_obj:
  asutarisu_txt = file_obj.read()
type(asutarisu_txt)
dict(asutarisu_txt)



import csv

with open("吹き矢の得点.csv", "r", encoding="utf-8") as file_obj:
    reader_obj = csv.reader(file_obj)
    for row in reader_obj:
        for i in range(1, 5):  # 1 要素ずつ取り出す
            row[i] = int(row[i])  # 整数型に変換
        print(sum(row[1:5]))




import json

with open("asutarisu.json", "w", encoding="utf-8") as f:
    json.dump(asutarisu, f)

with open("asutarisu.json", "r", encoding="utf-8") as f:
    asutarisu_json = json.load(f)
    type(asutarisu_json)