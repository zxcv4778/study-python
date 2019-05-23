사용자의 입력과 출력
====================

> 사용자 입력 -> 처리(프로그램, 함수 등) -> 출력

사용자 입력
-----------

input의 사용

<pre><code>
a = input()
print(a)

# 출력 결과
Life is too short, you need python.
</code></pre>

- input은 입력되는 모든 것을 문자열로 취급한다.

프롬프트를 띄워서 사용자 입력 받기

> input(질문 내용")

<pre><code>
b = input('숫자를 입력하세요!: ')
print(b)

# 출력 결과
숫자를 입력하세요!: 2
</code></pre>

print 자세히 알기
----------------

큰 따옴표로 둘러싸인 문자열은 + 연산과 동일하다

<pre><code>
print("life" "is" "too short")
print("life" + "is" + "too short")

# 출력 결과
lifeistoo short
lifeistoo short
</code></pre>

문자열 띄어쓰기는 콤마로 한다.

<pre><code>
print("life", 'is', 'too short')

# 출력 결과
life is too short
</code></pre>

한 줄에 결과값 출력하기

<pre><code>
for i in range(10):
    print(i, end=' ')

# 출력 결과
0 1 2 3 4 5 6 7 8 9 
</code></pre>