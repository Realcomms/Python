# 한줄 주석
"""
여러줄 주석
"""
result = 10
print(result)
result = 20
print(result)

print(10)
print(20)

# 상수 예제
print("---상수 예제---")
hello1 = "world"
world = "hello"

print(hello1)
print(world)

# if 문
print("---if 문---")
password = 1234
if password == 1234:
    print("문을 열어줍니다.")
else:
    print("아무 것도 하지 않습니다.")

# elif : 다중 if else
print("---elif : 다중 if else---")
score = 86

if score >= 90:
    print("A")
elif score >= 80:
    print("B")
else:
    print("C")

score = 77
if score >= 90:
    print("A")
elif score >= 80:
    print("B")
elif score >= 70:
    print("C")
else:
    print("F")
