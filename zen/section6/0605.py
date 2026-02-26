'''
zen.section6.0605 の Docstring
PP_06_05_リストの編集.ipynb
'''


# 要素の変更
ra_men = ["iekei", "soi", "solt", "miso", "tsukemen"]
ra_men[1] = 'soi_source'
print(ra_men)


# append
ra_men.append("aburasoba")
print(ra_men)


# extend
ra_men.extend(["tonkotsu", "othors"])
print(ra_men)


# insert
ra_men.insert(6, "tomato")
print(ra_men)


# remove
ra_men.remove("othors")
print(ra_men)


# pop
ra_men.pop()
print(ra_men)


# stacck
ra_men.pop(4)
print(ra_men)


# del
del ra_men[2]
print(ra_men)