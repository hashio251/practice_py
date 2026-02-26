'''
zen.section6.0604 の Docstring
PP_06_04_リストのメソッド.ipynb
'''


# reverse
'''
reverse メソッドを使って、 iroha リストの要素を逆順に並べ替えてください。
リストを表示して、中身を確かめてください。
'''
iroha = ['い', 'と', 'に', 'は', 'へ', 'ほ', 'ろ']
iroha.sort(reverse=True)
print(iroha)



# index
print(iroha.index('と'))



# copy
iroha_cp = iroha.copy()
print(iroha_cp)