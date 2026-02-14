# BMI

h = float(input("身長を入力してください。")) / 100
w = float(input("体重を入力してください。"))
bmi = w / h ** 2
print(f"あなたのBMIは {round(bmi, 2)} です。")

if bmi < 18.5:
    print("- やせすぎ -")
elif bmi < 25:
    print("- 標準体重 -")
elif bmi < 30:
    print("- 前肥満 -")
elif bmi < 35:
    print("- 肥満（1度） -")
elif bmi < 40:
    print("- 肥満（2度） -")
else:
    print("- 肥満（3度） -")