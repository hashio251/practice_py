'''
zen.section2.0206 の Docstring
演算の優先順位
演習問題
'''

'''
「大阪在住または京都在住で職場が大阪にある人」という条件について、 2 とおりの解釈を示し、それぞれの解釈をコードで表してください。

ただし、変数 居住地 と変数 勤務地 には、都道府県名が入っているものとします。
ここでは、大阪に住んでいて京都で働いている人を考えてみましょう。
'''
live_locate = "osaka"
work_locate = "kyoto"
live_locate == "osaka" or live_locate == "kyoto" and work_locate == "osaka"
(live_locate == "osaka" or live_locate == "kyoto") and work_locate == "osaka"