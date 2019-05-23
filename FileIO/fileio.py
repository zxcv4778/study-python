# 생성

# f = open('새 파일', 'w')
# f.close()

# nf = open('/Users/teddy/Desktop/새파일.txt', 'w')
# nf.close()

# 파일을 쓰기 모드로 열어 출력값 적기

# for i in range(1, 11):
#     data = "%d번째 줄입니다.\n" %i
#     nf.write(data)
# nf.close()

# readline

# nf = open('/Users/teddy/Desktop/새파일.txt', 'r')
# line = nf.readline()
# print(line)
# nf.close()

# while True:
#     line = nf.readline()
#     if not line:
#         break
#     print(line)
# nf.close()

# readlines

# nf = open('/Users/teddy/Desktop/새파일.txt', 'r')
# lines = nf.readlines()
#
# for line in lines:
#     print(line)
# nf.close()

# read

# nf = open('/Users/teddy/Desktop/새파일.txt', 'r')
# data = nf.read()
# print(data)
# nf.close()

# 파일에 새로운 내용 추가

# nf = open('/Users/teddy/Desktop/새파일.txt', 'a')
# for i in range(11, 20):
#     data = "%d번째 줄입니다.\n" %i
#     nf.write(data)
# nf.close()

# with

with open("/Users/teddy/Desktop/foo.txt", "w") as f:
    f.write("Life is too short, you need python!!!")
