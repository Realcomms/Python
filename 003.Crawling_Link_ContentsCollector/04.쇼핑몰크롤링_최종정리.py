"""
쇼핑몰 데이터 수집하기
페이징 되어 있는 데이터 어떻게 페이지별 전체 데이터를 수집해야 하는지 알아보기
"""

import requests
from bs4 import BeautifulSoup

# 함수1 - 상품정보
def get_product_info(vHtml):
    p_tag = vHtml.find("p", {"class": "name"})
    spans = p_tag.findAll("span")  # 제품명 - 리스트형식[배열]
    ul = vHtml.find("ul")  # 가격 - 리스트형식[배열]
    spans_price = ul.findAll("span")

    # return spans[0].text

    name = spans[0].text  # 제품명
    price = spans_price[0].text  # 가격
    atag = vHtml.find("a")
    link = atag['href']  # 링크 - 태그의 링크속성인 href속성값만 추출
    imgDiv = vHtml.find("div", {"class": "thumbnail"})
    imgTag = imgDiv.find("img")
    imgUrl = imgTag['src']  # 제품 이미지주소

    # 리턴은 한개 값만 보낼수 있기 때문에 여러개의 값을 딕셔너리를 활용해야 함
    return {"name": name, "price": price, "link": link, 'imgurl': imgUrl}
########################################################


# 함수2 - url따라 정보 가져오기 
def get_page_products(url):
    # requests 로 접근시 비정상적인 시도로 판단되어 403 Forbidden 에러 방지를 위해서 헤더 추가하여 처리
    header = {'User-Agent': 'Mozilla/5.0'}
    result = requests.get(url, headers=header)

    bs_obj = BeautifulSoup(result.content, "html.parser")
    # 전체 html 코드에서 뽑아내려 하는 데이터 영역 선택
    ul = bs_obj.find("ul", {"class": "prdList grid4"})

    # 상품명, 가격, 상세링크, 이미지경로 뽑기 - 함수1 사용함
    boxes = ul.findAll("div", {"class": "box"})
    product_info_list = [get_product_info(box) for box in boxes]

    return product_info_list
########################################################

"""
url = "http://jolse.com/category/toners-mists/1019/?page=1"
page_products = get_page_products(url)
print(page_products)
"""

# 규칙이 있는 url을 페이징 반복하여 실행 - 최종
url = "http://jolse.com/category/toners-mists/1019/?page="

for page_number in range(0, 11):
    print(page_number, sep='\n')
    page_products = get_page_products(url + str(page_number))  # 문자열로 형변환
    print(page_products, sep='\n')















