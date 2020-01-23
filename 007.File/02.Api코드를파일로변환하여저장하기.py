"""
    공공데이터 : www.data.go.kr
    API 정보 : 국내관광정보
    인증키 : j4l3iiE%2FWpJJkdFO9IFRI2IiIpgdYzJMEdpIpm7vx%2BEaug%2FfjuxAlH0pkVyFZA6tPIO20bO52C3y%2Fj4BgDSWfw%3D%3D
    아래 스크립트 결과(
"""
# 지역기반 관광정보 조회 : 메뉴얼에서 지역기반 관광정보 조회 오퍼레이션 명세 참고

import bs4
import requests

endpoint = 'http://api.visitkorea.or.kr/openapi/service/rest/RusService/areaBasedList?'
serviceKey = "j4l3iiE%2FWpJJkdFO9IFRI2IiIpgdYzJMEdpIpm7vx%2BEaug%2FfjuxAlH0pkVyFZA6tPIO20bO52C3y%2Fj4BgDSWfw%3D%3D"

# 파라미터 정의
numOfRows = "10"
pageSize = "1"
pageNo = "1"
MobileOS = "ETC"
MobileApp = "AppTest"
arrange = "A"
contentTypeId = "78"
areaCode = "4"
sigunguCode = "4"
listYN = "Y"

paramset = "serviceKey=" + serviceKey + "&" + "numOfRows=" + numOfRows + "&" + "pageSize=" + pageSize + \
    "&" + "pageNo=" + pageNo + "&" + "MobileOS=" + MobileOS + "&" + "MobileApp=" + MobileApp + \
    "&" + "arrange=" + arrange + "&" + "contentTypeId=" + contentTypeId + "&" + "areaCode=" + areaCode + \
    "&" + "sigunguCode=" + sigunguCode + "&" + "listYN=" + listYN

url = endpoint + paramset
print(url)

result = requests.get(url)
bs_obj = bs4.BeautifulSoup(result.content, "html.parser")
# print(bs_obj.findAll("title"))

# 파일에 데이터 쓰기
f = open("C:/Users/Administrator/Desktop/Work/Project_Python/007.File/국내관광정보API_Result.txt", "w", encoding='utf-8')  # 인코딩 명시
f.write(str(bs_obj.findAll("title")))  # 문자열로 변환
f.close()

