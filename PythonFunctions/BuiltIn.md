내장 함수
===========

abs
---------------

- 어떤 숫자를 입력으로 받았을 때, 그 숫자의 절대값을 돌려줌

<pre><code>
print(abs(3))
print(abs(-3))
print(abs(-1.2))

# 출력 결과
3
3
1.2
</code></pre>

all
---------------

- all(x). 반복 간으한 자료형을 인수로 받으며, 이 x가 모두 참이면 True, 아니면 False를 리턴.

<pre><code>
print(all([1,2,3]))
print(all([0,1,2,3]))

# 출력 결과
True
False
</code></pre>

any
---------------

- any(x) x중 하나라도 참이 있으면 True, 아니면 False

<pre><code>
print(all([1,2,3]))
print(all([0,1,2,3]))

# 출력 결과
True
True
</code></pre>

chr
---------------

- chr(i). 아스키 코드값을 입력으로 받아 그 코드에 해당하는 문자를 출력

<pre><code>
print(chr(48))
print(chr(97))

# 출력 결과
0
a
</code></pre>

dir
---------------

- dir. 객체가 자체적으로 가지고 있는 변수나 함수를 보여줌.

<pre><code>
print(dir([1,2,3,4]))
print(dir({1:'4'}))

# 출력 결과
['__add__', '__class__', '__contains__', ...]
['__class__', '__contains__', '__delattr__', ...]
</code></pre>

divmod
---------------

- divmod(a, b). 2개의 숫자를 입력으로 받는다.
- a를 b로 나눈 몫과 나머지를 튜플 형태로 리턴함.

<pre><code>
print(divmod(7, 3))
print(divmod(1.3, 0.2))

# 출력 결과
(2, 1)
(6.0, 0.09999999999999998)
</code</pre>

enumerate
---------------

- 순서가 있는 자료형을 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.

<pre><code>
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
    
# 출력 결과
0 body
1 foo
2 bar
</code></pre>

eval
---------------

- eval(expression). 실행 가능한 문자열을 입력받아 문자열을 실행한 결과값을 리턴.

<pre><code>
print(eval('3 + 4'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))

# 출력 결과
7
hia
(1, 1)
</code></pre>

filter
---------------

- 첫번째 인수로 함수 이름, 두번째 인수로 반복가능한 자료형이 들어감.
- 리턴값이 참인 것만 묶어서 돌려준다.

<pre><code>
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# 출력 결과
[1, 2, 6]
</code></pre>

hex
---------------

- hex(x). 정수값을 입력받아 16진수로 변환

<pre><code>
print(hex(234))
print(hex(255))

# 출력 결과
0xea
0xff
</code></pre>

id
---------------

- id(object). 객체를 입력받아 객체의 고유 주소값(레퍼런스)을 리턴.

<pre><code>
a = 3
print(id(3))
print(id(a))

b = a
print(id(b))

# 출력 결과
4455121088
4455121088
4455121088
</code></pre>

input
---------------

- input([prompt]). 사용자의 입력을 받는 함수.
- 입력 인수로 문자열을 주면 그 문자열은 프롬프트가 된다.

<pre><code>
c = input()
print(c)

d = input("Enter: ")
print(d)

# 출력 결과
a
Enter: rlemr
</code></pre>

int
---------------

- int(x). 문자열 형태의 숫자나 소수점이 있는 숫자 등을 정수 형태로 리턴.

<pre><code>
print(int('3'))
print(int(3.4))

# 출력 결과
3
3
</code></pre>

- int(x, radix). radix 진수로 표현된 문자열 x를 10진수로 변환하여 리턴

<pre><code>
print(int('11', 2))

# 출력 결과
3
</code></pre>

isinstance
---------------

- isinstance(object, class). 첫 번째 인수로 인스턴스, 두 번째 인수는 클래스 이름.
- 입력으로 받은 인스턴스가 그 클래스의 인스턴스인지를 판단.

<pre><code>
class Person: pass

ins = Person()
print(isinstance(ins, Person))

noins = 3
print(isinstance(noins, Person))

# 출력 결과
True
False
</code></pre>

lambda
---------------

- 함수를 생성할 때 사용하는 예약어로 def와 동일한 역할을 한다.

> lambda 인수 1, 인수 2, ...:

<pre><code>
sum = lambda a, b: a + b
print(sum(3, 4))

# 출력 결고
7
</code></pre>

len
---------------

- len(s). 입력값 s의 길이를 리턴

<pre><code>
print(len("python"))
print(len([1,2,3]))
print(len((1,'a')))

# 출력 결과
6
3
2
</code></pre>

list
---------------

- list(s). 반복 가능한 자료형 s를 입력받아 리스트로 만들어 리턴.

<pre><code>
print(list('python'))
print(list((1,2,3)))

# 출력 결과
['p', 'y', 't', 'h', 'o', 'n']
[1, 2, 3]
</code></pre>

map
---------------

- map(f, iterable). 함수 f와 반복 가능한(iterable) 자료형을 받음.
- 입력받은 자료형의 각 요소가 함수 f에 의해 수행된 결과를 묶어서 리턴.

<pre><code>
def two_times(x): return x * 2

print(list(map(two_times, [1,2,3,4])))

# 출력 결과
[2, 4, 6, 8]
</code></pre>

max
---------------

- max(iterable). 반복가능한 자료형을 입력받아 그 최대값을 리턴.

<pre><code>
print(max([1, 2, 3]))
print(max("python"))

# 출력 결과
3
y
</code></pre>

min
---------------

- min(iterable). max 함수와 반대.

<pre><code>
print(min([1, 2, 3, 4]))
print(min("python"))

# 츨력 결과
1
h
</code></pre>

oct
---------------

- oct(x). 정수 형태의 숫자를 8진수 문자열로 바꾸어 리턴.

<pre><code>
print(oct(34))
print(oct(123))

# 출력 결과
0o42
0o173
</code></pre>

ord
---------------

- orc(c). 문자의 아스키 코드값을 리턴.

<pre><code>
print(ord('a'))
print(ord('0'))

# 출력 결과
97
48
</code></pre>

pow
---------------

- pow(x, y). x의 y 제곱한 결과값을 리턴.

<pre><code>
print(pow(2, 4))
print(pow(3, 3))

# 출력 결과
16
27
</code></pre>

range
---------------

- range([start,], stop [,step]). 입력받은 숫자에 해당되는 범위의 값을 반복 가능한 객체로 만들어 리턴.

<pre><code>
print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))

# 출력 결과
[0, 1, 2, 3, 4]
[5, 6, 7, 8, 9]
[1, 3, 5, 7, 9]
</code></pre>

sorted
---------------

- sorted(iterable). 입력값을 정렬한 후 그 결과를 리스트로 리턴.

<pre><code>
print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))

# 출력 결과
[1, 2, 3]
['a', 'b', 'c']
</code></pre>

str
----------

- str(object). 문자열 형태로 객체를 변환하여 리턴.

<pre><code>
print(str(3))
print(str('hi'))
print(str('hi'.upper()))

# 출력 결과
3
hi
HI
</code></pre>

tuple
----------

- tuple(iterable). 반복 가능한 자료형을 입력받아 튜플 형태로 바꾸어 리턴.

<pre><code>
print(tuple("abc"))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))

# 출력 결과
('a', 'b', 'c')
(1, 2, 3)
(1, 2, 3)
</code></pre>

type
---------

- type(object). 입력값의 자료형이 무엇인지 알려주는 함수이다.

<pre><code>
print(type("abc"))
print(type([]))
print(type(open("test", 'w')))

# 출력 결과
<class 'str'>
<class 'list'>
<class '_io.TextIOWrapper'>
</code></pre>

zip
------

- zip(iterable*). 동일한 개수로 이루어진 자료형을 묶어주는 역할을 한다.

<pre><code>
print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))

# 출력 결과
[(1, 4), (2, 5), (3, 6)]
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
[('a', 'd'), ('b', 'e'), ('c', 'f')]
</code></pre>
