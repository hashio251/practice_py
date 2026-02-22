'''
zen.section5.0506 の Docstring
PP_05_06_変数のスコープ.ipynb
'''
# local
def number():
  num = [1, 2, 3, 4]
  print(num)

number()



# grobal
fruits = ["apple", "banana", "orange"]
def fruits_kinds():
  print(fruits)

fruits_kinds()