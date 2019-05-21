DataType
=========

Number
------------
1. 정수 : 124, -42, 0

2. 실수 : 123.45, -123.45, 3.4e10 (e, E  둘 다 가능)

4. 8진수 : 0o42, 0o25, 0o12

5. 16진수 : 0x2B, 0xFF

3. 복소수 : 1 + 2j, 4j, -10j
<pre><code>
# 복소수 관련 내장 함수
# 변수 a에 복소수 대입
a = 1 - 4j

# a의 실수
print(a.real)

# a의 허수
print(a.imag)

# a의 켤레복소수
print(a.conjugate())

# a의 절대값
print(a.__abs__())
</code></pre>


#### 숫자 연산자
- 기본적인 사칙연산 네가지
> 더하기 +, 빼기 - , 곱하기 *, 나누기 /
>> python 2.7 에서는 3 / 4 하면 정수형끼리 나누는 경우라 0이 출력된다.
>> python 3 에서는 3 / 4 하면 정수형끼리 나누더라도 실수형인 0.75로 출력된다. 
<pre><code>
# 변수 b, c에 정수형 대입
b = 3
c = 9

# +
print(b + c) # 12

# -
print(b - c) # -6

# *
print(b * c) # 27

# /
print(b / c) # 0.33333333333
</code></pre>

- 제곱 연산
> **
>> <pre><code> 
>> # ** 
>> print(b ** c) # 19683
>> </code></pre>

- 나눗셈 후 나머지 반환
> %
>> <pre><code>
>> # %
>> print(b % c) # 3
>> </code></pre>

- 나눗셈 후 소수점 아랫자리 버림
> //
>> <pre><code>
>> # //
>> print(b // c) # 0
>> </code></pre>


String
------------
- 문자열을 만드는데 4가지 방법이 존재한다.
<pre><code>
"SunPythonSon"
'SunPythonSon'
'''SunPythonSon'''
"""SunPythonSon"""

# 출력결과
SunPythonSon
SunPythonSon
SunPythonSon
SunPythonSon

</code></pre>

- 문자열 중간에 quote 삽입
<pre><code>
"Sun'Python'Son"
'SunPython"Son"'
"\'Sun\'PythonSon"
'SunPython\"Son\"'

# 출력결과
Sun'Python'Son
SunPython"Son"
'Sun'PythonSon
SunPython"Son"

</code></pre>

- 둘러싼 quote와 같은 quote를 문자열 중간에 썼을 때 SyntaxError가 발생한다.
<pre><code>
File "/Users/teddy/Desktop/sunpython/data_type/string_type.py", line 1
    title = "Sun"PythonSon"
                         ^
SyntaxError: invalid syntax

</code></pre>

- 여러줄 쓸 때
<pre><code>
print("Sun\nPython\nSon")

title = """Sun
Python
Son
"""
title1 = '''Sun
Python
Son
'''

print(title)
print(title1)

# 출력결과
Sun
Python
Son
Sun
Python
Son

Sun
Python
Son

# '''****''' single quotes로
# multi line string을 구성할 때 앞에 \n가 하나 들어감.
# .rstrip() 으로 해결 가능

</code></pre>

####문자열 연산

- 문자열 더하기
<pre><code>

sun = "Sun"
python = "Python"
son = "Son"

print(sun + python + son)

# 출력 결과
SunPythonSon

</code></pre>

- 문자열 곱하기
<pre><code>

print(python * 4)
print("=" * 50)
print("SunPythonSon")
print("*" * 50)

# 출력 결과
PythonPythonPythonPython
==================================================
SunPythonSon
**************************************************

</code></pre>

####문자열 인덱싱

- 문자열은 배열처럼 인덱싱 할 수 있다.

<pre><code>

strIndexing = "What is love?"

print(strIndexing[0])
print(strIndexing[4])
print(strIndexing[6])
print(strIndexing[-1])
print(strIndexing[-4])

# 출력 결과
W
 
s
?
o
</code></pre>

####문자열 슬라이싱

<pre><code>

strIndexing = "What is love?"

print(strIndexing[0:8])
print(strIndexing[5:7])
print(strIndexing[6:])
print(strIndexing[:])
print(strIndexing[8:-1])

# 출력 결과
What is 
is
s love?
What is love?
love

</code></pre>

####문자열 포매팅

<pre><code>
person = "Deuk"
print("%s love twice!" %person)

numberOfMembers = 9
print("Twice has %d members." %numberOfMembers)

sun = "Sun"
son = "Son"
print("%sPython%s" %(sun, son))

# 출력 결과
Deuk love twice!
Twice has 9 members.
SunPythonSon

</code></pre>

문자열 관련 내장 함수들
--------------
- 문자 개수 (count)

<pre><code>
sana = "sana"
print(sana.count("a"))

# 출력 결과
2

</code></pre>

- 위치 알려주기 (find)

<pre><code>

nsnl = "No Sana No Life"
print(nsnl.find("L"))
print(nsnl.find("W"))

# 출력 결과
11
-1

</code></pre>
> 없는 문자 혹은 문자열을 찾으려고 하면 -1을 리턴한다.

- 위치 알려주기 (index)

<pre><code>

nsnl = "No Sana No Life"
print(nsnl.index("e"))
print(nsnl.index("k"))

# 출력 결과
14
ValueError: substring not found

</code></pre>

- 문자열 삽입

<pre><code>
whiteSpace = " "
print(whiteSpace.join("1234"))

# 출력 결과
1 2 3 4
</code></pre>

- 소문자를 대문자로 (upper)

<pre><code>
sana = "sana"
nsnl = "No Sana No Life"

print(sana.upper())
print(nsnl.upper())

# 출력 결과
SANA
NO SANA NO LIFE
</code></pre>

- 대문자를 소문자로 (lower)

<pre><code>
sana = "sana"
nsnl = "No Sana No Life"

print(sana.lower())
print(nsnl.lower())

# 출력 결과
sana
no sana no life
</code></pre>

- 왼쪽 공백 지우기 (lstrip)

<pre><code>
nayeon = "Nayeon"
lovely = "%10s is lovely." %nayeon

print(lovely)
print(lovely.lstrip())

# 출력 결과
    Nayeon is lovely.
Nayeon is lovely.
</code></pre>

- 오른쪽 공백 지우기 (rstrip)

<pre><code>
parkName = "Yeontral Park"
schedule = "I'll going to %s.     " %parkName

print(schedule)
print(schedule.rstrip())

# 출력 결과
'I'll going to Yeontral Park.     '
'I'll going to Yeontral Park.'
</code></pre>

- 양쪽 공백 지우기 (strip)

<pre><code>
parkName = " Yeontral Park "

print(parkName)
print(parkName.strip())

# 출력 결과
' Yeontral Park '
'Yeontral Park'
</code></pre>

- 문자열 바꾸기 (replace(바뀌게 될 문자열, 바꿀 문자열))

<pre><code>
parkName = "Yeontral Park"

print(parkName.replace("Yeontral", "Deuk"))

# 출력 결과
Deuk Park
</code></pre>

- 문자열 나누기 (split)

<pre><code>
nsnl = "No Sana No Life"
print(nsnl.split())

chars = 'a:b:c:d'
print(chars.split(":"))

# 출력 결과
['No', 'Sana', 'No', 'Life']
['a', 'b', 'c', 'd']
</code></pre>

> 문자열은 나눈 다음 리스트에 차곡차곡 쌓아놓는다.

고급 문자열 포매팅
-----------------
- 숫자 바로 대입하기

<pre><code>
print("I eat {0} apples".format(4))

# 출력 결과
I eat 4 apples
</code></pre>

- 문자 바로 대입하기

<pre><code>
print("I eat {0} apples".format("four"))

# 출력 결과
I eat four apples
</code></pre>

- 변수로 대입하기
<pre><code>
numberOfApples = 104
print("I eat {0} apples".format(numberOfApples))

fruits = "pine apples"
print("I ate 500 {0}".format(fruits))

# 출력 결과
I eat 104 apples
I ate 500 pine apples
</code></pre>

- 2개 이상의 값 넣기

<pre><code>
numberOfApples = 104
fruits = "pine apples"

print("I ate {0} {1}.".format(numberOfApples, fruits))

# 출력 결과
I ate 104 pine apples.
</code></pre>

> 순서에 맞게 입력해야함

- 이름으로 넣기

<pre><code>
print("I ate {num} {meals}.".format(num=300, meals="eggs"))

# 출력 결과
I ate 300 eggs.
</code></pre>

> 인덱스랑 이름이랑 혼용해서 쓸 수도 있음
>> ex) I ate {0} {meals}.".format(300, meals="eggs")

- 왼쪽 정렬

<pre><code>
print("'{0:<10}'".format("hi"))

# 출력 결과
'hi        '
</code></pre>

- 오른쪽 정렬

<pre><code>
print("'{0:>10}'".format("hi"))

# 출력 결과
'        hi'
</code></pre>

- 가운데 정렬

<pre><code>
print("'{0:^20}'".format("hello world"))

# 출력 결과
'    hello world     '
</code></pre>

- 공백 채우기

<pre><code>
print("{0:=^20}".format("hello world"))
print("{0:@>20}".format("hello world"))
print("{0:!<20}".format("hello world"))

# 출력 결과
====hello world=====
@@@@@@@@@hello world
hello world!!!!!!!!!
</code></pre>

- 소수점 표현하기

<pre><code>
pi = 3.141592
print("{0:0.4f}".format(pi))
print("'{0:10.4f}'".format(pi))

# 출력 결과
3.1416
'    3.1416'
</code></pre>

- '{' 혹은 '}' 표현하기

<pre><code>
print("{{ and }}".format())

# 출력 결과
{ and }
</code></pre>