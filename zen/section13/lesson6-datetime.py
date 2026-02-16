import datetime
from datetime import datetime

now = datetime.now()
print(f"今日は{now.year}年{now.month}月{now.day}日です。\n現在時刻は{now.hour}時{now.minute}分{now.second}秒です。")


import os

statinfo = os.stat("lesson3-file.py")

statinfo.st_size
statinfo.st_mtime
datetime.fromtimestamp(statinfo.st_mtime)