"""
[함수정의 방법]
def로 시작하고, 엔터를 사용하여 함수와 실행하는 부분 간격(줄)을 2줄 이상 띄워야 함
예) def aaaa():
    print("hello");
"""


def print_hello():
    print("hello")


print_hello()


def print_message(p_message):
    print(p_message)


print_message("안녕하세요.")


def pikachu(skill_number):
    if skill_number == 1:
        print("전기공격")
    elif skill_number == 2:
        print("몸통박치기")


pikachu(2)


# Return

def plus(val1, val2):
    return val1 + val2


result_return = plus(10,20)
print("result:", result_return)

# 리턴이 없는 경우 None으로 출력됨


def print_hello2(p1, p2):
    print("using print:", p1 + p2)


def plus2(val1, val2):
    return val1 + val2


result2 = print_hello2(10, 20)
result_return = plus2(10, 20)

print("result:", result2)
print("result_return", result_return)
