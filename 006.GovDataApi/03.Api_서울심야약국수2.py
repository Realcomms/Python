"""
    공공데이터 : www.data.go.kr
    API 정보 : 전국 약국정보 조회
    인증키 : j4l3iiE%2FWpJJkdFO9IFRI2IiIpgdYzJMEdpIpm7vx%2BEaug%2FfjuxAlH0pkVyFZA6tPIO20bO52C3y%2Fj4BgDSWfw%3D%3D

# 한글 인코딩

from urllib.parse import quote

seoul = "서울특별시"
print(seoul)

seoul = quote(seoul)
print(seoul)
"""

from urllib.parse import quote
import requests
import bs4

endpoint = "http://apis.data.go.kr/B552657/ErmctInsttInfoInqireService/getParmacyListInfoInqire?"  # 요청주소
serviceKey = "j4l3iiE%2FWpJJkdFO9IFRI2IiIpgdYzJMEdpIpm7vx%2BEaug%2FfjuxAlH0pkVyFZA6tPIO20bO52C3y%2Fj4BgDSWfw%3D%3D"  # 인증키

Q0 = quote("서울특별시")
ORD = "NAME"
pageNo = "1"
startPage = "1"
numOfRows = "10"

paramset = "serviceKey=" + serviceKey + "&" + "Q0=" + Q0 + "&" + "ORD=" + ORD + \
           "&" + "pageNo=" + pageNo + "&" + "startPage=" + startPage + "&" + "numOfRows=" + numOfRows


url = endpoint + paramset
print("url : " + url)

result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")  # 이때 대문자를 모두 소문자로 변환됨
items = bs_obj.findAll("item")

count = 0
for item in items:
    tagged_item = item.find("dutytime1c")  # dutyTime1c

    if (tagged_item != None):
        close_time = int(tagged_item.text)
        if (close_time > 1800):
            count += 1

print("월요일 6시 이후까지 하는 약국의 수 : " + str(count))

