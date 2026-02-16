import csv

file_obj = open("吹き矢の得点.csv", "r", encoding="utf-8")
reader_obj = csv.reader(file_obj)
list(reader_obj)
file_obj.close()

with open("吹き矢の得点.csv", "r", encoding="utf-8") as file_obj:
  reader_obj = csv.reader(file_obj)
  list(reader_obj)

with open("吹き矢の得点.csv", "r", encoding="utf-8") as file_obj:
  reader_obj = csv.reader(file_obj)
  for row in reader_obj:
      print(row)

with open("吹き矢の得点.csv", "r", encoding="utf-8") as file_obj:
    file_obj.read()