import requests, bs4
r = requests.get("https://google.com")
print(r.text)
print(r.text[-7:])
soup = bs4.BeautifulSoup(r.text, "html.parser")
print(soup.title)
print(soup.title.string)

r2 = requests.get("https://google.com/maps")
soup = bs4.BeautifulSoup(r2.text, "html.parser")
print(soup.title.string)