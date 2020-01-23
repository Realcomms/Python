"""
 네이버 검색 API
 Client ID : WEWT2Q1oriVzGf6fWB6b
 Client Secret : kzi2z4046P

 json 형식 온라인으로 보기 : http://jsonviewer.stack.hu/

 requests 라이브러리 사용하여 소스코드 줄이기
"""

# 네이버 검색 API예제는 블로그를 비롯 전문자료까지 호출방법이 동일하므로 blog검색만 대표로 예제를 올렸습니다.
# 네이버 검색 Open API 예제 - 블로그 검색
import requests
from urllib.parse import urlparse

client_id = "WEWT2Q1oriVzGf6fWB6b"
client_secret = "kzi2z4046P"

# 함수로 묶기


def get_api_result(keyword, display, start):
    url = "https://openapi.naver.com/v1/search/blog?query=" + keyword + "&display=" + str(display) + "&start=" + str(start)  # json 결과
    result = requests.get(urlparse(url).geturl(),
                        headers = {
                                "X-Naver-Client-Id": client_id,
                                "X-Naver-Client-Secret": client_secret
                        }
                      )
    return result.json()  # json 형식으로 변환하여 출력


def call_and_print(keyword, page):
    json_obj = get_api_result(keyword, 100, page)
    for item in json_obj['items']:
        print(item)


"""
API 호출한 후, 필요한 데이터 뽑아내기
"""
keyword = "강남역"
json_obj = get_api_result(keyword, 100, 101)

"""
print("display:", json_obj['display'])
print("start:", json_obj['start'])
print("items count:", len(json_obj['items']))
# print(json_obj['items'])
"""

for item in json_obj['items']:
    # print(item)
    # print(item['title'])
    # print(item['title'].replace("<b>", "").replace("</b>", ""))
    print(item['title'].replace("<b>", "").replace("</b>", ""), item['link'])



