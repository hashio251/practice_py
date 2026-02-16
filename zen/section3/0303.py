'''
zen.section3.0303 の Docstring
match文
'''


# ワイルドカード
'''
前回の授業で、季節の名前を英語で表示するコードを書きました。
'''
season = "春"
match season:
    case "春":
        print("Spring")
    case "夏":
        print("Summer")
    case "秋":
        print("Fall")
    case "冬":
        print("Winter")
    case _:
        print("Other season")



# 「または」のパターン
'''
以下のコードの、 2 つ目の case の "雨" という値を、「"雨" または "あめ" または "アメ"」というパターンに変更してください。
'''
wether = "あめ"
match wether:
    case "晴" | "はれ" | "ハレ":
        print("Sunny")
    case "雨" | "あめ" | "アメ":
        print("Rainy")
    case "曇":
        print("Cloudy")
    case _:
        print("Other weather")



# 「～を含む」のパターン
'''
以下のコードに case を追加して、天気に "雪" が含まれるとき、"Snowy" と表示されるようにしてください。
'''
wether = "大雪"
match wether:
    case x if "曇" in x:
        print("Cloudy")
    case x if "風" in x:
        print("Windy")
    case x if "雪" in x:
        print("Snowy")
    case _:
        print("Other weather")



# pass 文
'''
以下のコードを実行すると、エラーが発生します。
コードを編集して、エラーが発生しないようにしてください。
'''
wether = "晴"
match wether:
    case "曇":
        print("Cloudy")
    case "雷":
        pass
    case _:
        print("Other weather")