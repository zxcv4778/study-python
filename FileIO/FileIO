FileIO
==================

파일 생성
------------

<pre><code>
f = open('새 파일', 'w')
f.close()
</code></pre>

> 파일 객체 = open(파일 이름, 파일 열기 모드)

- 파일 열기 모드에는 3 가지가 있다.
1. r: 읽기 모드 -> 파일을 읽기만 할 때 사용  
2. w: 쓰기 모드 -> 파일에 내용을 쓸 때 사용  
3. a: 추가 모드 -> 파일의 마지막에 새로운 내용을 추가할 때 사용

- 만약 파일을 다른 디렉터리에 생성하고 싶다면 다음과 같이 작성해야 한다.

<pre><code>
nf = open('/Users/teddy/Desktop/새파일.txt', 'w')
nf.close()
</code></pre>

- 터미널을 열어 해당 경로로 들어가 확인해보면 새파일.txt 가 있다.

파일을 쓰기 모드로 열어 출력값 적기
-------------------------------

<pre><code>
for i in range(1, 11):
    data = "%d번째 줄입니다.\n" %i
    nf.write(data)
nf.close()

# 새파일.txt

1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
</code></pre>

프로그램의 외부에 저장된 파일을 읽는 여러가지 방법
-----------------------------------------

readline() 함수 이용하기

<pre><code>
nf = open('/Users/teddy/Desktop/새파일.txt', 'r')
line = nf.readline()
print(line)
nf.close()

# 출력 결과
1번 쨰 줄입니다.
</code></pre>

- 모든 라인을 읽어들이고 싶다면

<pre><code>
while True:
    line = nf.readline()
    if not line:
        break
    print(line)
nf.close()

# 출력 결과
1번째 줄입니다.

2번째 줄입니다.

3번째 줄입니다.

4번째 줄입니다.

5번째 줄입니다.

6번째 줄입니다.

7번째 줄입니다.

8번째 줄입니다.

9번째 줄입니다.

10번째 줄입니다.

</code></pre>

readlines() 함수 이용하기

<pre><code>
lines = nf.readlines()

for line in lines:
    print(line)
nf.close()

# 출력 결과
1번째 줄입니다.

2번째 줄입니다.

3번째 줄입니다.

4번째 줄입니다.

5번째 줄입니다.

6번째 줄입니다.

7번째 줄입니다.

8번째 줄입니다.

9번째 줄입니다.

10번째 줄입니다.

</code></pre>

- 위의 코드에서 lines는 파일의 모든 라인을 읽어서 각각의 줄을 요소로 같는 리스트를 리턴한다.

read() 함수 이용하기

<pre><code>
nf = open('/Users/teddy/Desktop/새파일.txt', 'r')
data = nf.read()
print(data)
nf.close()

# 출력 결과
1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
</code></pre>

- 파일의 전체 내용을 문자열로 리턴한다.

파일에 새로운 내용 추가하기
-------------------------

<pre><code>
nf = open('/Users/teddy/Desktop/새파일.txt', 'a')
for i in range(11, 20):
    data = "%d번째 줄입니다.\n" %i
    nf.write(data)
nf.close()

# 새 파일.txt

1번째 줄입니다.
2번째 줄입니다.
3번째 줄입니다.
4번째 줄입니다.
5번째 줄입니다.
6번째 줄입니다.
7번째 줄입니다.
8번째 줄입니다.
9번째 줄입니다.
10번째 줄입니다.
11번째 줄입니다.
12번째 줄입니다.
13번째 줄입니다.
14번째 줄입니다.
15번째 줄입니다.
16번째 줄입니다.
17번째 줄입니다.
18번째 줄입니다.
19번째 줄입니다.
</code></pre>

with문과 함께 사용하기
-----------------------
- 파일을 닫을 때 항상 .close() 를 사용해 왔는데 이를 자동으로 처리할 수 있음.

<pre><code>
with open("/Users/teddy/Desktop/foo.txt", "w") as f:
    f.write("Life is too short, you need python!!!")
    
# foo.txt
Life is too short, you need python!!!
</code></pre>

- with 문을 벗어나는 순간 파일 객체가 자동으로 close 된다.

sys 모듈로 입력 인수 주기
---------------------------

- 파이썬에서는 sys라는 모듈을 이용하여 입력 인수를 직접 줄 수 있다.

<pre><code>
import sys

args = sys.argv[1:]
for i in args:
    print(i)
</code></pre>

- 이 프로그램을 터미널에서 입력 인수를 주어 실행시키면 다음과 같다.

> cd ~/해당 디렉토리  
> python sys1.py aaa bbb ccc  
> aaa  
> bbb  
> ccc

- 다른 예시를 하나 더 작성해보자

<pre><code>
args = sys.argv[1:]
for i in args:
    if i == args[-1]:
        print(i.upper(), end='\n')
    else:
        print(i.upper(), end=' ')
</code></pre>

- 해당 프로그램을 터미널에서 실행시키면 다음과 같다.

> python3 sys1.py life is too short, you need python.  
> LIFE IS TOO SHORT, YOU NEED PYTHON.
