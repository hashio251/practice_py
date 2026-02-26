'''
zen.section6.0602 の Docstring
PP_06_02_インデックスとスライス.ipynb
'''


# 正のインデックス
'''
変数 numbers に、英語の数の名前を代入します。
numbers = ["one", "two", "three", "four", "five", "six", "seven"]
インデックスを使って、 "three" を参照してください。
'''
numbers = ["one", "two", "three", "four", "five", "six", "seven"]
print(numbers[2])



# 負のインデックス
'''
負のインデックスを使って、numbers リストの最後の要素を参照してください。
'''
print(numbers[-1])



# 連続するインデックス
'''
スライスを使って、numbers リストの 2 番目から 5 番目の要素を取り出してください。
5 番目の要素である "five" も含めてください。
'''
print(numbers[1:5])



# リストの先頭
'''
numbers リストの、最初の 4 個の要素を取り出してください。
'''
print(numbers[:4])



# リストの後尾
'''
numbers リストの、 4 番目の要素以降をすべて取り出してください。
'''
print(numbers[3:])


'''
numbers リストの、最後の 3 個の要素を取り出してください。
'''
print(numbers[-3:])



'''
スライスを使って、numbers リストから、1 番目、4 番目、7 番目の要素を取り出してください。
要素のインデックスは 3 ずつ増えています。
'''
print(numbers[::3])