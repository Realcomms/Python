# 문자열

crawling = "Data crawling is fun"
parsing = 'Data parsing is also fun'

print(crawling)
print(parsing)
print(type(crawling))
print(type(parsing))

# 문자열 합치기
print(crawling + " " + parsing)

# 형변환하여 합치기 ( **은 제곱의 의미임)
print("20 ** 3 : **의 의미 : " + str(20 ** 3))

r = 10
pie = 3.141592
area = (r ** 2) * pie
print("원의 넓이 : " + str(area))

# 문자열 인덱싱(0부터 시작)
data = crawling[0:4]
data_crawling = crawling[0:13]
fun = crawling[17:]
n = crawling[19]
n_range = crawling[-1:]
also = parsing[16:16 + 4]

print("---문자열 인덱싱---")
print(data)
print(data_crawling)
print(fun)
print(n)
print(n_range)
print(also)

# 자주사용하는 문자열 함수 - find()
print("# 자주사용하는 문자열 함수 - find()")
print(crawling.find("Data"))
print(crawling.find("fun"))
print(parsing.find("Data"))
print(parsing.find("fun"))
print(crawling.find("parsing"))
print(parsing.find("crawling"))

if crawling.find("aaa") == -1:
    print("aaa가 문자열에 없음")
else:
    print("aaa가 문자열에 있음")

# 자주사용하는 문자열 함수 - split()
print("# 자주사용하는 문자열 함수 - split()")
str_data = "random:data:choice:sampling:mini-batch:unpooling:training"
split_str_data = str_data.split(":")
print(str_data)
print(split_str_data)

for i in range(0, len(split_str_data)):
    print(split_str_data[i])

# 자주사용하는 문자열 함수 - replace()
print("# 자주사용하는 문자열 함수 - replace()")
print(crawling.replace("search", "analyze"))
print(crawling.replace("Data", "Web"))

# 자주사용하는 문자열 함수 - count()
print("# 자주사용하는 문자열 함수 - count()")
cnn_article = "After being impeached, President Donald Trump is hoping to move quickly to a vigorous defense in the Senate and is distressed the trial he hopes will vindicate him might be delayed.\"What are they doing?\" Trump asked a top Republican ally, Sen. Lindsey Graham, upon learning Thursday morning that House Democrats may withhold sending articles of impeachment to the Senate until they feel assured there will be a fair trial.\"I said, 'Mr. President, I don't know,'\" Graham told reporters before traveling to the White House to discuss the matter further with Trump.The uncertainty threw a wrench into long-laid plans by the White House to mount an effort at exoneration once the impeachment proceedings move across Capitol Hill to the upper chamber. Trump and his aides have long eyed a Senate trial as the venue for eventual vindication in the saga, viewing the Republican-led chamber as a lock to acquit the President.One possible avenue for Trump is looking back, to Barack Obama, with a suggestion -- supported possibly with Justice Department legal opinions -- that the former president should have been impeached for blocking congressional Republicans from fully investigating the \"Fast and Furious\" gun-running scandal."
print(cnn_article)
print("Trump 단어는 총 : " + str(cnn_article.count("Trump")) + "번 노출됨!!!")