import requests, bs4

my_url = "https://www.chickenramen.jp/hiyokochan/"
r = requests.get(my_url)
soup = bs4.BeautifulSoup(r.content, "html.parser")

soup.select("title")
for t in soup.select("h2"):
  print(t)

