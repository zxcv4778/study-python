LIST
==========

여러 언어에서 여러 이름으로 불리는데, 보통 배열 혹은 리스트라 불린다.

다른 프로그래밍 언어에서도 그렇듯 인덱스는 0부터 시작이다.

생성
--------

-  listName = [arg1, arg2, arg3]

리스트의 인덱싱과 슬라이싱
---------------------

####리스트의인덱싱

- 문자열과 인덱싱 방식이 같다.
- 인덱스 -1은 리스트의 마지막 인덱스와 같다.
- 인덱스가 가리키는 값이 같은 타입이면 연산이 가능하다.

<pre><code>
list = [1, 2, 3, 4, 'list', 'hello']

print(list[0] + list[3])
print(list[4] + list[5])
print(list[-1])

# 출력결과
5
listhello
hello
</code></pre>

- 만약 가리키는 인덱스가 리스트의 마지막 인덱스보다 크다면 IndexError 발생

<pre><code>
list = [1, 2, 3, 4, 'list', 'hello']

print(list[9])

# 출력결과
IndexError: list index out of range
</code></pre>

- 리스트 내부에 리스트를 추가하여 이중 리스트를 만드는 것도 가능하다.
> ex) list1 = [2, 4, 5, ['twice', 'izone']]

- 리스트 내부에 있는 리스트에서 값을 꺼내오고 싶을 때.

<pre><code>
list1 = [2, 4, 5, ['twice', 'izone']]

print(list1[-1][0])
print(list1[-1][1])

# 출력결과
twice
izone
</code></pre>

####리스트의 슬라이싱

- 인덱싱과 같이 문자열과 쓰임이 같다.

<pre><code>
list = [1, 2, 3, 4, 'list', 'hello']

print(list[:3])
print(list[3:])

# 출력결과
[1, 2, 3]
[4, 'list', 'hello']
</code></pre>

리스트 연산자
---------------

####리스트 더하기

<pre><code>
listA = [1, 2, 3]
listB = [4, 5, 6]

print(listA + listB)

# 출력결과
[1, 2, 3, 4, 5, 6]
</code></pre>

####리스트 반복하기

<pre><code>
listA = [1, 2, 3]
listB = [4, 5, 6]

print(listA * 3)
print(listB * 3)

# 출력결과
[1, 2, 3, 1, 2, 3, 1, 2, 3]
[4, 5, 6, 4, 5, 6, 4, 5, 6]
</code></pre>

리스트의 수정, 변경, 삭제
---------------------

####리스트에서 하나의 값 수정

<pre><code>
listA = [1, 2, 3]
listB = [4, 5, 6]

listA[1] = 9
listB[2] = 0

print(listA)
print(listB)

# 출력결과
[1, 9, 3]
[4, 5, 0]
</code></pre>

####리스트에서 연속된 범위의 값 수정하기

<pre><code>
listA[1:2] = ['twice', 'izone']
listB[1] = ['once', 'wizone']

print(listA)
print(listB)

# 출력결과
[1, 'twice', 'izone', 3]
[4, ['once', 'wizone'], 0]
</code></pre>

- 같은 자리에서 수정을 하더라도 방식이 다르다.
> listA[1:2]로 수정을 할 땐 list[1] 과 list[2] 사이의 리스트를 수정하는 의미인데 반해
> listB[1]로 수정을 할 땐 해당 요소를 바꾼다는 의미이다.

####[]로 리스트 요소 삭제하기

<pre><code>
listA[0:1] = []
print(listA)

listA[2:3] = []
print(listA)

# 출력결과
['twice', 'izone', 3]
['twice', 'izone']
</code></pre>

####del 함수를 이용하여 리스트 요소 삭제하기

<pre><code>
del listB[0]
print(listB)

del listB[-1]
print(listB)

# 출력결과
[['once', 'wizone'], 0]
[['once', 'wizone']]
</code></pre>

리스트 관련 내장함수
-----------------

####리스트에 요소 추가(append)

<pre><code>
twice = ['나연']
twice.append('사나')
twice.append('미나')
twice.append('지효')
twice.append('다현')

print(twice)

# 출력결과
['나연', '사나', '미나', '지효', '다현']
</code></pre>

####리스트 정렬(sort)

<pre><code>
numbers = [8, 3, 2, 0]
numbers.sort()

print(numbers)

# 출력결과
[0, 2, 3, 8]
</code></pre>

####리스트 뒤집기(reverse)

<pre><code>
twice.reverse()

print(twice)

# 출력결과
['다현', '지효', '미나', '사나', '나연']
</code></pre>

- 정렬은 안한다.

####위치 반환(index)

<pre><code>
print(twice.index('사나'))
print(twice.index('나연'))

# 출력결과
3
4
</code></pre>

- 없는 요소를 찾으려 할 때 ValueError 발생

<pre><code>
nationalAssembly = ['돈', '권력', '체면', '꼰대']

print(nationalAssembly.index('상식'))

# 출력결과
ValueError: '상식' is not in list
</code></pre>

####리스트 요소 삽입(insert)

<pre><code>
nationalAssembly.insert(0, '개판')

print(nationalAssembly)

# 출력결과
['개판', '세금', '권력', '체면', '꼰대']
</code></pre>

####리스트 요소 제거(remove)

<pre><code>
nationalAssembly.remove('체면')

print(nationalAssembly)

# 출력결과
['개판', '세금', '권력', '꼰대']
</code></pre>

####리스트 요소 끄집어내기(pop)

<pre><code>
print(nationalAssembly.pop(0))
print(nationalAssembly)

# 출력결과
개판
['세금', '권력', '꼰대']
</code></pre>

####리스트에 포함된 요소 x의 개수 세기(count)

<pre><code>
print(twice.count('나연'))

# 출력결과
1
</code></pre>

####리스트 확장(extend)

<pre><code>
twice.extend(['모모', '정연', '채영', '쯔위'])
print(twice)

# 출력결과
['다현', '지효', '미나', '사나', '나연', '모모', '정연', '채영', '쯔위']
</code></pre>


