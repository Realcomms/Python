# 정수(int)/실수(float)
# 정수를 나누기 하면 무조건 실수형으로 변경됨(소수점 .0)

a = 10
b = -20
c = 30
total = a + b + c
print(total)

a = 12.5
b = 35.8
c = 50
total = a + b + c
average = total / 3
print(average)

print(30/4)
print(4/30)
print(5/10)
print(10/5)
print(1/1)
print(type(1))
print(type(1/1))

# 연산자
print(5 + 4)
print(5.0 - 3.0)
print(10.5 * 4)
print(200 / 10)
print(200 % 10)

# 나누기
print(20 / 7)

# 나눈 나머지
print(20 % 7)

# 정수부분만 추출(소수점 이하 버림)
print(20 // 7)

# 중간고사 점수 비교 실습
A_Kor = 88
A_Eng = 76
A_Math = 95
B_Kor = 100
B_Eng = 67
B_Math = 80

A_Average = (A_Kor + A_Eng + A_Math) / 3
B_Average = (B_Kor + B_Eng + B_Math) / 3

# 조건문에서 파이참에서 괄호는 안해도 됨(밑줄이 그런 의미임. 파이참 옵션에서 없앨수 있지만 그냥 둠)
if A_Average > B_Average:
    print("A가 높아요.")
elif (A_Average == B_Average):
    print("서로 같아요.")
else:
    print("B가 높아요.")