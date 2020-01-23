# urllib 사용 : 웹에서 데이터를 받아오려면 http request라는 요청을 보내서 받아와야 함
# 파이썬에서 웹의 특정 주소로 요청을 보내는 기능이 urllib.request
# 만약, urllib 작동이 안되면, File > settings 에서 프로젝트에 urllib5 추가할것

import urllib.request
import bs4

# 웹에서 웹주소로 html코드 가져오기
url = "https://www.naver.com/"
html = urllib.request.urlopen(url)
# print(html.read())

# 가져온 html코드를 뷰티풀솝을 활용하여 파싱
bs_obj = bs4.BeautifulSoup(html, "html.parser")
# print(bs_obj)
# find로 찾을때는 값으로 표현되지만,
top_right = bs_obj.find("div", {"class":"area_links"})
print(top_right)

# findAll로 찾으면 리스트형식([])으로 값이 출력됨 - find와 차이점을 이해해야 함
top_right2 = bs_obj.findAll("div", {"class":"area_links"})
print(top_right2)

# 위에서 찾은 결과값에서 첫번째 a 태그의 값(text) 찾기
first_a = top_right.find("a").text
print(first_a)

# 네이버 메뉴 이름 뽑아내기(응용)
print("# 네이버 메뉴 이름 뽑아내기(응용)")
ul = bs_obj.find("ul", {"class":"an_l"})
print(ul)

# 1. ul안의 li만 뽑기
print("# 1. ul안의 li만 뽑기")
for i in ul:
    print(i)

# 2. 1번 결과물에서 빈칸이 있어 더 정교하게 뽑기 : 리스트형식([])으로 뽑기
print("# 2. 1번 결과물에서 빈칸이 있어 더 정교하게 뽑기")
ul2 = bs_obj.find("ul", {"class":"an_l"})
lis = ul2.findAll("li")
print(lis)

# 3. 2번 결과물에서 리스트형식을 for문 이용하여 [] 괄호 및 콤마(,) 제거하여 출력하기
print("# 3. 2번 결과물에서 리스트형식을 for문 이용하여 [] 괄호 및 콤마(,) 제거하여 출력하기")
for ii in lis:
    print(ii)

# 4. 3번 결과물에서 li 태그 안에 있는 a 태그 뽑기
print("# 4. 3번 결과물에서 li 태그 안에 있는 a 태그 뽑기")
for ii in lis:
    a_tag = ii.find("a")
    print(a_tag)

# 5. 4번 결과물에서 a 태그 안의 sapn 태그중 class가 an_txt 값만 뽑기
print("# 5. 4번 결과물에서 a 태그 안의 sapn 태그중 class가 an_txt 값만 뽑기")
for ii2 in lis:
    a_tag2 = ii2.find("a")
    span = a_tag2.find("span", {"class":"an_txt"})
    print(span.text)
















