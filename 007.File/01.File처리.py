"""
    파일 처리
"""

# 파일에 데이터 쓰기
f = open("C:/Users/Administrator/Desktop/Work/Project_Python/007.File/sample_data.txt", "w")
data = "easy_python_crawler"
f.write(data)
f.close()

# 파일의 데이터 읽어오기
f = open("C:/Users/Administrator/Desktop/Work/Project_Python/007.File/sample_data.txt", "r")
for str in f.readlines():
    print(str)
f.close()
