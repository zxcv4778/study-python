FUNCTION
============

- 중복 코드를 줄이기 위해서 사용
- 프로그램의 흐름을 일목요연하게 볼 수 있다.

함수의 구조
-------------

<pre><code>
def sum(a, b):
    return a + b
</code></pre>

<pre><code>
a = 3
b = 5
c = sum(a, b)

print(c)

# 출력 결과
5
</code></pre>

입력값과 결과값에 따른 함수의 형태
----------------------------

일반적인 함수

<pre><code>
def 함수명(인수):
    수행할 문장
    ....
    return 결과값
</code></pre>

- 입력값과 결과값이 있는 함수의 사용법은 다음과 같다.

> 결과값을 받을 변수 = 함수명(입력 인수1, 입력 인수2, ..)

입력값이 없는 함수

<pre><code>
def say():
    return 'Hi'
</code></pre>

<pre><code>
hi = say()

print(hi)

# 출력 결과
Hi
</code></pre>

- 입력값이 없고 결과값만 있는 함수는 다음 과 같이 사용된다.

> 결과값을 받을 변수 = 함수명()

결과값이 없는 함수

<pre><code>
def sum2(a,b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))

sum2(3, 4)

# 출력 결과
3, 4의 합은 7입니다.
</code></pre>

- 결과값이 없는 함수는 다음과 같이 사용한다.

> 함수명(입력인수 1, 입력인수 2, ...)

입력값도 결과값도 없는 함수

<pre><code>
def say2():
    print('Hello world')

say2()

# 출력 결과
Hello world
</code></pre>

- 입력값도 결과값도 없는 함수는 다음과 같이 사용한다.

> 함수명()

입력값이 몇 개가 될지 모를 때
----------------------------

여러 개의 입력값을 받는 함수 만들기

<pre><code>
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
        
    return sum
    
result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(result)

# 출력 결과
55
</code></pre>

- 입력 변수명 앞에 *를 붙이면 입력값들을 전부 모아서 튜플로 만들어 준다.

<pre><code>
def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i
        
    return sum
    
result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(result)

# 출력 결과
55
</code></pre>

<pre><code>
def sum_mul(choice, *args):
    if choice == 'sum':
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i

    return result

resultSum = sum_mul("sum", 1, 2, 3, 4, 5)
resultMul = sum_mul('mul', 1, 2, 3, 4, 5,)

print(resultSum)
print(resultMul)

# 출력 결과
15
120
</code></pre>

함수의 결과값은 언제나 하나이다.
---------------------------

<pre><code>
def sum_and_mul(a, b):
    return a + b, a * b

resultSM = sum_and_mul(3, 4)

print(resultSM)

# 출력 결과
(7, 12)
</code></pre>

- 튜플 값으로 준다.
- 각자 다른 값으로 받길 바란다면 아래와 같이 하면 된다.

> sum, mul = sum_and_mul(3, 4)

<pre><code>
def sum_and_mul(a, b):
    return a + b
    return a * b

resultSM = sum_and_mul(3, 4)

print(resultSM)

# 출력 결과
7
</code></pre>

- 함수는 return을 만나면 결과값을 반환하고 바로 빠져나온다.

입력 인수에 초깃값 미리 설정하기
------------------------------

<pre><code>
def say_myself(name, old, man=True):
    print('나의 이름은 %s입니다.' %name)
    print('나이는 %d살 입니다.' %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("marcus", 28)

# 출력 결과
나의 이름은 marcus입니다.
나이는 28살 입니다.
남자입니다.
</code></pre>

<pre><code>
say_myself('민지', 25, False)

# 출력 결과
나의 이름은 민지입니다.
나이는 25살 입니다.
여자입니다.
</code></pre>

주의 사항

- 초기값을 주고 싶은 인수는 항상 뒤쪽에 위치 해야한다.
- 그렇지 않으면 SyntaxError가 발생한다.

<pre><code>
def say_myself2(name, man=True, old):
    print('나의 이름은 %s입니다.' %name)
    print('나이는 %d살 입니다.' %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself2("marcus", 28)

# 출력 결과
SyntaxError: non-default argument follows default argument
</code></pre>