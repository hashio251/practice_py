import requests, bs4

my_url = "https://www.kahaku.go.jp/exhibitions/permanent/index.html"
r = requests.get(my_url)
soup = bs4.BeautifulSoup(r.content, "html.parser")
type(soup)

soup.select("title")
soup.select("img")
for e in soup.select("img"):
    print(e)
for a in soup.select("a"):
    print(a)


soup.select(".title_box_yellow")

soup.select("p")
soup.select(".bold")

for e in soup.select(".bold"):
    print(e)

for e in soup.select(".bold"):
    print(e.getText())