"""
특정 웹사이트에서 링크정보 가져오기
"""
import requests
from bs4 import BeautifulSoup


# 함수 생성


def get_bp_info(val):
    result = requests.get(val)
    bs_obj = BeautifulSoup(result.content, "html.parser")

    profile_name = bs_obj.find("div", {"class": "profile-name"})

    h1_bp_name = profile_name.find("h1")
    bp_name = h1_bp_name.text

    cover_buttons = bs_obj.find("div", {"class": "cover-buttons"})

    button_label = bs_obj.find("span", {"class": "button-label"})
    location = button_label.text

    lis = cover_buttons.findAll("li")
    li_tag = lis[1]

    a_tag = li_tag.find("a")
    link = a_tag['href']

    """
    dictionary1 = { }
    dictionary1['name'] = bp_name
    dictionary1['location'] = location
    dictionary1['link'] = link
    """
    # 위 딕셔너리 생성을 아래와 같이 한줄로 표현하기
    dictionary1 = {'name': bp_name, 'location': location, 'link': link}

    return dictionary1


url = "https://bp.eosgo.io/"

result = requests.get(url=url)
bs_obj = BeautifulSoup(result.content, "html.parser")

lf_items = bs_obj.findAll("div", {"class": "lf-item"})

hrefs = [div.find("a")['href'] for div in lf_items]

# dic_result = get_bp_info(hrefs[0])

for number in range(0, 5):
    dic_result = get_bp_info(hrefs[number])
    print(dic_result)
