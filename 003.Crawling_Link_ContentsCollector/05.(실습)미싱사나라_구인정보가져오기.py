"""
미싱사나라.com 구인정보 데이터 수집하기
가이드 - 페이징 전체(회사로고, 지역, 업종, 제목, 회사명, 상세링크)
"""

import requests
from bs4 import BeautifulSoup


# 함수는 위에서부터 순차적으로 존재해야 실행되므로 아래와 같은 순서로 정의하여 사용함


# 함수4 - 지역, 업종, 제목, 회사명, 상세링크 정보 가져오기
def get_recruit_info_detail(tr):
    tds = tr.findAll("td")

    link = tds[0].find("a")['href']  # 상세링크
    area = tds[1].find("a").text  # 지역
    gubun = tds[2].find("a").text  # 업종
    title = tds[3].find("span", {"class": "_option_span"}).text  # 제목
    company = tds[4].find("a").text  # 회사명

    # 리턴은 한개 값만 보낼수 있기 때문에 여러개의 값을 딕셔너리를 활용해야 함
    return {"area": area, "gubun": gubun, "title": title, "company": company, "link": link}
########################################################


# 함수3 - 여러개의 tr 처리
def get_recruit_info(trs):
    recruit = []  # 리스트 생성
    # for i in trs:
    for i in range(0, len(trs)):
        recruit.append(get_recruit_info_detail(trs[i]))  # 리스트에 상세정보 추가
        # recruit = trs
    return recruit
########################################################


# 함수2 - url 정보 가져오기
def get_page_info(url):
    # requests 로 접근시 비정상적인 시도로 판단되어 403 Forbidden 에러 방지를 위해서 헤더 추가하여 처리
    header = {'User-Agent': 'Mozilla/5.0'}
    result = requests.get(url, headers=header)

    bs_obj = BeautifulSoup(result.content, "html.parser")

    # 전체 html 코드에서 뽑아내려 하는 데이터 영역 선택
    target_div = bs_obj.find("div", {"class": "adver_box_title"})
    trs = target_div.find("table").findAll("tr", {"align": "center"})  # 반복되는 구문

    # return len(trs)
    # recruit_list = [get_recruit_info(trs) for i in trs]  # 리스트 형식으로 재변환
    recruit_list = get_recruit_info(trs)  # 리스트형식임
    return recruit_list
########################################################


# 정보를 가져오려고 하는 url
url = "http://미싱사나라.com/employ/index.php?page="

for page_number in range(0, 10):
    # print(page_number, sep='\n')
    recruit_info = get_page_info(url + str(page_number))  # 문자열로 형변환
    # print(recruit_info, sep='\n')
    
    # 최종결과 포맷 : [{'area',~~ }, {'area',~~ } ~~] 이런 형식의 리스트형식[] 안에 딕셔너리 포함
    # print(recruit_info)
    for i in range(0, len(recruit_info)):
        # print(recruit_info[i])
        result = recruit_info[i]  # 딕셔너리에서 값 추출
        print ("지역 : " + result["area"] + "/" + "업종 : " + result["gubun"] + "/" + "제목 : " + result["title"] + "/" + "회사명 : " + result["company"] + "/" + "링크 : " + result["link"])









