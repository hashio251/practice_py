import random

# omikuji
def draw_omikuji():
    omikuji = ["大吉", "中吉", "小吉", "吉", "凶", "大凶"]
    result = random.choice(omikuji)

    if result == "大吉":
        message = "超ラッキー！今日も一日頑張ろう！"
    elif result == "中吉":
        message = "ラッキー！今日も一日頑張ろう！"
    elif result == "小吉":
        message = "小さなラッキーがあるかも？！今日も一日頑張ろう！"
    elif result == "吉":
        message = "何事もちりつも！今日も一日頑張ろう！"
    elif result == "凶":
        message = "小さなアンラッキーでも落ち込まないで！明日はいい日になるかも？今日も一日頑張ろう！"
    else:
        message = "アンラッキー💦でも落ち込まないで！明日はいい日になるかも？今日も一日頑張ろう！"

    return result, message