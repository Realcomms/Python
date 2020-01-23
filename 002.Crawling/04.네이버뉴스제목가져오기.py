# urllib 사용 : 웹에서 데이터를 받아오려면 http request라는 요청을 보내서 받아와야 함
# 파이썬에서 웹의 특정 주소로 요청을 보내는 기능이 urllib.request
# 만약, urllib 작동이 안되면, File > settings 에서 프로젝트에 urllib5 추가할것

import urllib.request
import bs4

# 웹에서 웹주소로 html코드 가져오기
url = "http://news.naver.com/"
html = urllib.request.urlopen(url)

# 가져온 html코드를 뷰티풀솝을 활용하여 파싱
bs_obj = bs4.BeautifulSoup(html, "html.parser")
# print(bs_obj)

# 방식 1 - 네이버 헤드라인 뉴스 제목만 가져오기 : 공백이 있음 - find()
print("# 방식 1 - 네이버 헤드라인 뉴스 제목만 가져오기 : 공백이 있음")
naver_title = bs_obj.find("div", {"class":"hdline_article_tit"})
# print(naver_title)
for i in naver_title:
    a_tag = naver_title.find("a")
    print(a_tag.text)

# 방식 2 - 네이버 헤드라인 뉴스 제목만 가져오기 : 공백 없이 제목만 - findAll(), strip() 앞뒤공백제거함수
print("# 방식 2 - 네이버 헤드라인 뉴스 제목만 가져오기 : 공백 없이 제목만 - findAll()")
news_title = bs_obj.findAll("a", {"class":"lnk_hdline_article"})
print(news_title)
for i in news_title:
    print(i.text.strip())









