# 반복문 예제
for item in range(0,10):
    print(item)

for item in range(0, 10):
    print("Hello")

# 리스트 예제
list_number = [0, 1, 2, 3, 4, 5]
list_string = ["Seoul", "Busan", "Daegu"]
print(list_number)
print(list_string)


# 리스트에서 인덱스로 아이템 선택하기
num_list = [0, 1, 2, 2, 4]
print(num_list)
print(num_list[3])

# for로 리스트 출력하기
for item in [0, 1, 2, 3, 4]:
    print(item)

# 구구단 만들기
print(2, 1, 2)
print(2, "*", 1, "=", 2)

for num in range(1, 10):
    print(2, num)

for item in range(1, 10):
    print(2, "*", item, "=", 2 * item)

# for문을 바로 리스트로 만들기
num_list = [1, 2, 3, 4]

# num_list 각각에 2를 곱한 결과
print("# num_list 각각에 2를 곱한 결과")
for num in num_list:
    print(num * 2)

num_lt = [1, 2, 2, 4]

# num_lt 각각에 2를 곱한 결과(다시 list 형태로 만드는 방법)
resultCom = [num * 2 for num in num_lt]
print(resultCom)

