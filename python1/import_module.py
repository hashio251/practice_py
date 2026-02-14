# create calendar

import calendar, time

def create_calendar(year=None, month=None):
  t = time.localtime()
  year = year or t.tm_year
  month = month or t.tm_mon
  print(f"今日は {year} 年 {month} 月 {t.tm_mday} 日 {t.tm_hour}時 {t.tm_min} 分だよ")
  print(f"今月のカレンダー\n {calendar.month(year, month)} ")
create_calendar()
user_year, user_month = int(input("表示したい年を入力してください。")), int(input("表示したい月を入力してください。"))
create_calendar(user_year,user_month)