from urllib.request import urlopen

url = "http://www.hycu.ac.kr"
html = urlopen(url)

print(html.read())
