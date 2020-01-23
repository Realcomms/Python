import json
json_str = '[{"name": "korea", "age": "22"}, {"name": "seoul", "age": "52"}]'
json_obj = json.loads(json_str)  # 위 처럼 json 형태로 되어 있는 text를 json 오브젝트로 변경(생성)
"""
print(json_obj)  # [] 리스트 형태로 출력
print(json_obj[0])  # {} 딕셔너리 형태로 출력
print(json_obj[0:2])  # 리스트 인덱스가 0번보다는 크고 2번 보다는 작은 '0,1' 인덱스 2개를 출력하라는 의미임
print(json_obj[0]["name"])
print(json_obj[1]["age"])

# 반복문을 사용하여 가져오기
for aaa in json_obj:
    print(aaa)
"""
for bbb in json_obj:
    # print(bbb["name"], bbb["age"])  # print 쓸때, 콤마(,)를 이용해 여러개의 값을 출력하기
    print(bbb["name"] + "," + bbb["age"])


