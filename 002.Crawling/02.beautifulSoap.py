# 뷰티풀숍 - 파싱 라이브러리
import bs4
html_str = "<html><div>hello</div></html>"
bs_obj = bs4.BeautifulSoup(html_str, "html.parser")

print(type(bs_obj))
print(bs_obj)
print(bs_obj.find("div"))

print("# 예제1")
html_str2 = """
    <html>
        <body>
            <ul>
                <li>hello</li>
                <li>bye</li>
                <li>welcome</li>
            </ul>
        </body>
    </html>
"""

bs_obj2 = bs4.BeautifulSoup(html_str2, "html.parser")
ul = bs_obj2.find("ul")
print(ul)

print("# 전체에서 li를 찾을때 첫번째 것만 나옴")
li = bs_obj2.find("li")
print(li)

print("# li 전체를 찾고 싶을때 - find_all : 리스트형식으로 출력됨")
li2 = ul.find_all("li")
print(li2)

print("# li 태그 안에 있는 텍스트만 뽑으려면...")
li_text = bs_obj2.find("li")
print(li_text.text)

# findAll() 사용하기 : 조건에 해당하는 모든 요소를 리스트형식([])으로 추출
html_str3 = """
<html>
    <body>
        <ul>
            <li>hello</li>
            <li>bye</li>
            <li>welcome</li>
        </ul>
    </body>
</html>
"""
print("# findAll() 사용하기 : 조건에 해당하는 모든 요소를 리스트형식([])으로 추출")
bs_findAll = bs4.BeautifulSoup(html_str3, "html.parser")
ul_findAll = bs_findAll.find("ul")
li_findAll = bs_findAll.findAll("li")
print(li_findAll)

# 인덱스로 데이터 접근하기
print("# 인덱스로 데이터 접근하기")
print(li_findAll[1])
print(li_findAll[2].text)

# 데이터 뽑을때 class 속성 이용하기
print("# 데이터 뽑을때 class 속성 이용하기")
html_str4 = """
    <html>
        <body>
            <ul class="greet">
                <li>hello</li>
                <li>bye</li>
                <li>welcome</li>                
            </ul>
            <ul class="reply">
                <li>ok</li>
                <li>no</li>
                <li>sure</li>
            </ul>
        </body>
    </html>
"""
bs_obj4 = bs4.BeautifulSoup(html_str4, "html.parser")

ul4 = bs_obj4.find("ul")
print(ul4)

ul4_1 = bs_obj4.find("ul", {"class":"reply"})
print(ul4_1)

# 속성값 뽑아내기
print("# 속성값 뽑아내기")
html_str5 = """
    <html>
        <body>
            <ul class="ko">
                <li>
                    <a href="https://www.naver.com/">네이버</a>
                </li>
                <li>
                    <a href="https://www.daum.net/">다음</a>
                </li>
            </ul>
            <ul class="sns">
                <li>
                    <a href="https://www.google.com/">구글</a>
                </li>
                <li>
                    <a href="https://www.facebook.com/">페이스북</a>
                </li>
            </ul>
        </body>        
    </html>
"""
print("-첫번째 a 태그 뽑아내기")
bs_obj5 = bs4.BeautifulSoup(html_str5, "html.parser")
atag = bs_obj5.find("a")
print(atag)

print("-첫번째 a 태그의 href 속성으로 값을 뽑기")
print(atag['href'])














