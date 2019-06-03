예외처리
=============

오류는 어떤 때 발생하는가
--------------------

<pre><code>

# FileNotFoundError

f = open("error", 'r')

# ZeroDivisionError

print(4 / 0)

# IndexError

a = [1, 2, 3]
print(a[4])
</code></pre>

예외 처리 기법
--------------

> try:  
>   ...  
> except[발생 오류[as 오류 메시지 변수]]:  
>   ...
>> [] 안에 있는 메시지는 필수는 아니다.

<pre><code>
# FileNotFoundError

try:
    f = open("foo.txt", 'r')
except FileNotFoundError as e:
    print(e)
else:
    data = f.read()
    f.close


# ZeroDivisionError

try:
    print(4 / 0)
except ZeroDivisionError as e:
    print(e)

# IndexError

try:
    a = [1, 2, 3]
    print(a[4])
finally:
    print("The Final")
    
# 출력 결과
[Errno 2] No such file or directory: 'foo.txt'
division by zero
The Final
...
IndexError: list index out of range
</code></pre>

- try ... else
    * 예외가 발생하지 않을 경우에 else 실행.
- try ... finally
    * 예외 발생 여부에 상관없이 finally 수행.
    
오류 회피하기
-------------

> pass

- 에러가 발생해도 무시한다.

<pre><code>
try:
    f = open("no file", 'r')
except FileNotFoundError:
    pass
</code></pre>

오류 일부러 발생시키기
-----------------

> raise

- 에러를 강제로 발생시킨다.

<pre><code>
class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()

# 출력 결과
...
NotImplementedError
</code></pre>