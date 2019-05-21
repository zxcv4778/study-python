# 문자열 생성
print("SunPythonSon")
print('SunPythonSon')
print('''SunPythonSon''')
print("""SunPythonSon""")

# 문자열 안에 quote 삽입
print("Sun'Python'Son")
print('SunPython"Son"')
print("\'Sun\'PythonSon")
print('SunPython\"Son\"')

# 여러 줄 쓸 때
print("Sun\nPython\nSon")

title = """Sun
Python
Son
"""
title1 ='''Sun
Python
Son
'''

print(title.rstrip('\r\n'))
print(title1.rstrip('\r\n'))

# 문자열 더하기
sun = "Sun"
python = "Python"
son = "Son"

print(sun + python + son) # SunPythonSon

# 문자열 곱하기

print(python * 4) # PythonPythonPythonPython

print("=" * 50)
print("SunPythonSon")
print("*" * 50)

# 문자열 인덱싱

strIndexing = "What is love?"

print(strIndexing[0])
print(strIndexing[4])
print(strIndexing[6])
print(strIndexing[-1])
print(strIndexing[-4])

# 문자열 슬라이싱

print(strIndexing[0:8])
print(strIndexing[5:7])
print(strIndexing[6:])
print(strIndexing[:])
print(strIndexing[8:-1])

# 문자열 포매팅
person = "Deuk"
print("%s love twice!" %person)

numberOfMembers = 9
print("Twice has %d members." %numberOfMembers)

print("%sPython%s" %(sun, son))

# count

sana = "sana"
print(sana.count("a"))

# find

nsnl = "No Sana No Life"
print(nsnl.find("L"))
print(nsnl.find("W"))

# index

print(nsnl.index("e"))
# print(nsnl.index("k"))

# join

whiteSpace = " "
print(whiteSpace.join("1234"))

# upper

print(sana.upper())
print(nsnl.upper())

# lower

print(sana.lower())
print(nsnl.lower())

# lstrip

nayeon = "Nayeon"
lovely = "%10s is lovely." %nayeon

print(lovely)
print(lovely.lstrip())

# rstrip

parkName = "Yeontral Park"
schedule = "I'll going to %s.     " %parkName

print(schedule)
print(schedule.rstrip())

# strip

print(parkName)
print(parkName.strip())

# replace

print(parkName.replace("Yeontral", "Deuk"))

# split

print(nsnl.split())

chars = 'a:b:c:d'

print(chars.split(":"))

# format(num)

print("I eat {0} apples".format(4))

# format(str)

print("I eat {0} apples".format("four"))

# format(var)

numberOfApples = 104
print("I eat {0} apples".format(numberOfApples))

fruits = "pine apples"
print("I ate 500 {0}".format(fruits))

# format(var, var)

print("I ate {0} {1}.".format(numberOfApples, fruits))

# format(name)

print("I ate {num} {meals}.".format(num=300, meals="eggs"))

# advanced lstrip

print("'{0:<10}'".format("hi"))

# advanced rstrip

print("'{0:>10}'".format("hi"))

# advanced strip

print("'{0:^20}'".format("hello world"))

# fill blank

print("{0:=^20}".format("hello world"))
print("{0:@>20}".format("hello world"))
print("{0:!<20}".format("hello world"))

# floating point

pi = 3.141592
print("{0:0.4f}".format(pi))
print("'{0:10.4f}'".format(pi))

# '{' or '}'

print("{{ and }}".format())
