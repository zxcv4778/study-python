모듈
=============

- 함수나 변수 또는 클래스 들을 모아 놓은 파일.

모듈 생성 및 불러오기
-----------------

> import 모듈이름

<pre><code>
# mod1.py

def sum(a, b):
    return a + b

def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 있는 것이 아닙니다.")
        return
    else:
        result = sum(a, b)

    return result

---------------------

# module.py

import mod1

print(mod1.sum(4, 5))
print(mod1.safe_sum(3, 4))
print(mod1.safe_sum(3, '4'))

# 출력 결과

9
7
더할 수 있는 것이 아닙니다.
None
</code></pre>

모듈의 이름을 붙이지 않고 해당 모듈의 함수를 바로 사용할 수도 있다.

> from 모듈이름 import 모듈함수

<pre><code>
# mod1.py

def sum(a, b):
    return a + b

def safe_sum(a, b):
    if type(a) != type(b):
        print("더할 수 있는 것이 아닙니다.")
        return
    else:
        result = sum(a, b)

    return result

---------------------

# module.py

from mod1 import sum, safe_sum

print(sum(4, 5))
print(safe_sum(3, 4))
print(safe_sum(3, '4'))

# 출력 결과

9
7
더할 수 있는 것이 아닙니다.
None
</code></pre>

if \__name\__ == "\__main\__": 의 의미
----------------------------------------

- 다른 파일에서 모듈을 불러 쓸 때 해당 모듈의 출력문 등을 실행시키지 않는다.
- 주로 모듈을 테스트하기 위해 사용.

<pre><code>
if __name__ == "__main__":
    print(sum(4, 5))
    print(safe_sum(4,3))
    print(safe_sum(4, '4'))
</code></pre>

클래스나 변수 등을 포함한 모듈
----------------------------

<pre><code>
# mod2.py

PI = 3.141592

class Math:
    def solv(self, r):
        return PI * (r ** 2)

def sum(a, b):
    return a + b

if __name__ == "__main__":
    print(PI)
    a = Math()
    print(a.solv(3))
    print(sum(PI, 4.4))

---------------------

# module.py

import mod2

print(mod2.PI)

a = mod2.Math()
print(a.solv(2))
print(mod2.sum(mod2.PI, 4.4))

# 출력 결과

3.141592
12.566368
7.5415920000000005
</code></pre>

