import csv

file_obj = open("restaurant.csv", "w", encoding="utf-8", newline="")
writer_obj = csv.writer(file_obj)

writer_obj.writerow(["菊屋", "和食", "唐揚げ", "1,000"])
writer_obj.writerow(["エスパーニャ", "スペイン料理", "パエリヤ", "2,000"])
file_obj.close()



file_obj = open("restaurant.csv", "a", encoding="utf-8", newline="")
writer_obj = csv.writer(file_obj)
writer_obj.writerow(["Panda Garden", "中華料理", "北京ダック", "1,500"])
file_obj.close()

with open("レストラン.csv", "a", encoding="utf-8", newline="") as file_obj:
  writer_obj = csv.writer(file_obj)
  writer_obj.writerow(["ボーノ", "イタリア料理", "マルゲリータ", "2,000"])