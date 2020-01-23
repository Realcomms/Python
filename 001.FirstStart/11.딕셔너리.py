# 딕셔너리 : {}, 리스트는 []
# 딕셔너리는 리스트와 달리 순서가 없다는 것, 값(value)를 접근하기 위해서는 키(key)로만 가능

user = {}
print(user)
print(type(user))

user2 = {"name":"Kims", 0:"aaa", 1:"bbb"}
print(user2)
print(user2["name"])
print(user2[0])
print(user2[1])

# 딕셔너리에 여러개 값 넣기
naver = {
    "name":"naver",
    "url":"www.naver.com",
    "userid":"aaa",
    "passwd":"!@#SDFAadfas"
}

google = {
    "name":"google",
    "url":"www.google.com",
    "userid":"bbb",
    "passwd":"%@#sadfasd"
}
print(naver)
print(type(naver))
print(google)
print(type(google))

# 딕셔너리 사용하기
print(naver["url"])
print(google["name"])

# 딕셔너리에 데이터 추가
site = {
    "naver" : "www.naver.com",
    "google" : "www.google.com"
}

site["daum"] = "www.daum.net"
print(site)
print(site["daum"])

site["yahoo"] = "www.yahoo.com"
print(site)
print(site["yahoo"])

# 딕셔너리에 있는 데이터 수정하기
site["daum"] = "www.aaa.net"
print(site)

# 딕셔너리에 있는 데이터 삭제하기
del site["daum"]
print(site)

# 자주 사용하는 딕셔너리 함수 - get()
print("# 자주 사용하는 딕셔너리 함수 - get()")
site2 = {
    "naver" : "www.naver.com",
    "google" : "www.google.com"
}

print(site.get("naver"))
print(site.get("daum"))

insert_key = "daum"
if (site.get(insert_key) == None):
    print(insert_key + "에 대한 데이터가 없습니다.")

# 자주 사용하는 딕셔너리 함수 - keys(), values(), items()
print("# 자주 사용하는 딕셔너리 함수 - keys(), values(), items()")
site3 = {
    "naver" : "www.naver.com",
    "google" : "www.google.com",
    "daum" : "www.daum.net"
}

print(site.keys())
print(site.values())
print(site.items())

for key in site.keys():
    print(key)
for value in site.values():
    print(value)
for item in site.items():
    print(item)

# 리스형으로 변경
print("# 리스형으로 변경")
print(list(site.keys()))



