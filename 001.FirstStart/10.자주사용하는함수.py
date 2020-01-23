# 자주사용하는 리스트 함수
print("# 자주사용하는 리스트 함수 - append, insert")
int_list2 = [1, 2, 3, 4, 5]
int_list2.append(6)
print(int_list2)
int_list2.insert(0, -1)
print(int_list2)

print("# 자주사용하는 리스트 함수 - remove, del")
int_list3 = [1, 2, 3, 4, 5, 4]
int_list3.remove(4)
print(int_list3)

del int_list3[3:]
print(int_list3)

print("# 자주사용하는 리스트 함수 - sort")
int_list4 = [3, 4, 2, 8, 1, 7]
float_list4 = [4.4, 2.2, 3.3, 5.5, 1.1]
string_list4 = ["Java", "Asp", "Php", "Jquery", "Python"]
int_list4.sort()
float_list4.sort()
string_list4.sort()

print(int_list4)
print(float_list4)
print(string_list4)

print("# 자주사용하는 리스트 함수 - count")
int_list5 = [1, 5, 4, 3, 7, 5, 4, 2, 4]
string_list5 = ["car", "cat", "can", "cut", "cat", "cnn", "cure", "cat"]
print(int_list5.count(4))
print(string_list5.count("cat"))


