VARIABLE
==========

- 변수
- 객체를 가리키는 것.

생성
-----------

> 변수명 = 변수에 저장할 값

- 변수는 객체가 저장된 메모리의 위치를 가리킨다.
- reference

<pre><code>
a = 3
b = 5

print(type(3))

# 출력 결과
<class 'int'>
</code></pre> 

- 3은 상수가 아닌 정수형 객체이다.
- a = 3 을 선언하면 a.real을 바로 쓸 수 있다. 

- 동일한 객체인지 판단하기 위해서 is 를 사용할 수 있다.

<pre><code>
print(a is b)
print(b is c)

# 출력 결과
False
True
</code></pre>

- 튜플이나 리스트로 변수를 만들 수 있다.

<pre><code>
twice, izone = 'once', 'wizone'
[once, wizone] = ['twice', 'izone']
t = i = 'girlgroup'
</code></pre>

- 두 변수의 값을 바꿀 수 있다.

<pre><code>
a, b = b, a

print(a)
print(b)

# 출력 결과
5
3
</code></pre>

레퍼런스 카운팅(getrefcount)

<pre><code>
import sys

print(sys.getrefcount(3))
print(sys.getrefcount(5))

# 출력 결과
50
28
</code></pre>

변수의 복사
-----------

- 같은 객체가 아닌 서로 다른 객체를 가리키게 할 수 있다.

[:] 이용

<pre><code>
listA = [1, 2, 3]
listB = listA[:]

listA[1] = 4

print(listA)
print(listB)

# 출력 결과
[1, 4, 3]
[1, 2, 3]
</code></pre>

copy 모듈 이용

<pre><code>
from copy import copy

listC = copy(listA)
print(listA is listC)

# 출력 결과
False
</code></pre>