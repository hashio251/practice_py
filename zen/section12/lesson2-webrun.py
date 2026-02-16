import webbrowser

webbrowser.open("https://www.google.com")
webbrowser.open_new("https://youtube.com")
webbrowser.open_new_tab("https://x.com")
webbrowser.open_new_tab("https://instagram.com")

url_list = [
    "https://youtube.com",
    "https://facebook.com",
    "https://instagram.com"
]
webbrowser.open_new(url_list[0])
for url in url_list[1:]:
  webbrowser.open_new_tab(url)


chrome_path = "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome"
browser = webbrowser.Chrome(chrome_path)
browser.open_new("https://google.com")
browser.open_new_tab("https://youtube.com")