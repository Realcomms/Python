# 리스트
name = []
print(name)
print(type(name))

name2 = ["Seoul"]
print(name2)

# 리스트 만들기
int_list = [1, 2, 3, 4, 5]
float_list = [1.1, 2.2, 3.3, 4.4, 5.5]
string_list = ["Seoul", "Daejeon", "Daegu", "Busan", "Jeju"]
all_list = [int_list, float_list, string_list]

print(int_list)
print(float_list)
print(string_list)
print(all_list)

# 리스트에서 데이터 순서로 접근하기
print(int_list[2:4])
print(float_list[-1:])
print(string_list[1])
print(all_list[0][4])

# for 문을 활용한 리스트
print("# for 문을 활용한 리스트")
for i in range(0, len(int_list)):
    print(int_list[i])

for i in range(0, len(float_list)):
    print(float_list[i])

for i in range(0, len(string_list)):
    print(string_list[i])

for i in range(0, len(all_list)):
    print(all_list[i])



