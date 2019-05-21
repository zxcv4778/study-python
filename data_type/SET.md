SET
==========

- 집합에 관련된 것들을 처리

생성
-------

- 리스트를 입력하여 만들거나

<pre><code>
s1 = set([1, 2, 3])
print(s1)

# 출력 결과
{1, 2, 3}
</code></pre>

- 문자열을 입력하여 만들 수 있다.

<pre><code>
s2 = set("Hello world")
print(s2)

# 출력 결과
{'w', ' ', 'r', 'l', 'H', 'o', 'd', 'e'}
</code></pre>

특징
--------------

- 중복을 허용하지 않는다.
- 순서가 없다.
- 리스트 혹은 튜플로 변환 가능

<pre><code>
l1 = list(s1)
print(l1)

t1 = tuple(s1)
print(t1)

# 출력 결과
[1, 2, 3]
(1, 2, 3)
</code></pre>

집합 자료형을 활용하는 방법
-------------------------

교집합

<pre><code>
s3 = set([1, 3, 5, 2, 4, 6])
s4 = set([3, 5, 7, 2, 9, 0])

print(s3 & s4)

# 출력 결과
{2, 3, 5}
</code></pre>

- intersection 함수를 사용해도 같은 결과가 나온다.

<pre><code>
print(s3.intersection(s4))

# 출력 결과
{2, 3, 5}
</code></pre>

합집합

- 중복해서 포함된 값은 한 개씩만 나온다.

<pre><code>
print(s3 | s4)

# 출력 결과
{0, 1, 2, 3, 4, 5, 6, 7, 9}
</code></pre>

- union 함수 사용 가능

<pre><code>
print(s3.union(s4))

# 출력 결과
{0, 1, 2, 3, 4, 5, 6, 7, 9}
</code></pre>

차집합

<pre><code>
print(s3 - s4)

# 출력 결과
{1, 4, 6}
</code></pre>

- difference 함수 사용 가능

<pre><code>
print(s3.difference(s4))

# 출력 결과
{1, 4, 6}
</code></pre>

집합 자료형 관련 내장함수
---------------------

값 1개 추가하기(add)

<pre><code>
s3.add(8)
print(s3)

# 출력 결과
{1, 2, 3, 4, 5, 6, 8}
</code></pre>

값 여러 개 추가하기(update)

<pre><code>
s3.update([11, 21, 31])
print(s3)

# 출력 결과
{1, 2, 3, 4, 5, 6, 8, 11, 21, 31}
</code></pre>

특정 값 제거하기(remove)

<pre><code>
s3.remove(11)
print(s3)

# 출력 결과
{1, 2, 3, 4, 5, 6, 8, 21, 31}
</code></pre>















