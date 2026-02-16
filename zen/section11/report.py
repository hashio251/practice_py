import csv

with open("snow.csv", "r", encoding="shift-jis") as file_obj:
  reader_obj = csv.reader(file_obj)
  row = list(reader_obj)
print(row[:1])
print(row[1:5])