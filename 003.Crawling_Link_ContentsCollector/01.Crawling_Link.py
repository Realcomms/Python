"""
특정 웹사이트에서 링크정보 가져오기
"""
import requests
from bs4 import BeautifulSoup

url = "https://bp.eosgo.io/"

result = requests.get(url=url)
bs_obj = BeautifulSoup(result.content, "html.parser")

# 링크를 포함하고 있는 엘리먼트 추출
lf_items = bs_obj.findAll("div", {"class":"lf-item"})
# print(lf_items)

# 링크가 있는 엘리먼트 추출 - lf_items 리스트에서 div만 뽑아서 그중에 a태그가 있는 엘리먼트중 href만 값을 추출하기 - 리스트형식으로 결과값 생성
hrefs = [div.find("a")['href'] for div in lf_items]
print(hrefs)
# print(len(hrefs)) - 개수 함수 len()
# print(hrefs[0:5])
# print(len(hrefs[0:5]))





