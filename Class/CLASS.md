CLASS
==================

class 기초
-------------

class 변수

<pre><code>
class Service:
    secret = "영구는 배꼽이 두 개다."

pey = Service()

print(pey.secret)

# 출력 결과
영구는 배꼽이 두 개다.
</code></pre>

class 함수

<pre><code>
class Service:
    secret = "영구는 배꼽이 두 개다."

    def sum(self, a, b):
        result = a + b
        print("%s + %s = %s입니다." %(a, b, result))

pey = Service()
pey.sum(1, 1)

# 출력 결과
1 + 1 = 2입니다.
</code></pre>

self

- 클래스 내의 클래스 함수는 첫번째 argument로 self를 받아야만 한다.

<pre><code>
class Service:
    secret = "영구는 배꼽이 두 개다."

    def setName(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." %(self.name, a, b, result))

pey = Service()
pey.setName("Marcus")
pey.sum(1, 1)

# 출력 결과
Marcus님 1 + 1 = 2입니다.
</code></pre>

\__init\__ 이란 무엇인가

- 인스턴스를 만들 때 항상 실행된다.

<pre><code>
class Service1:
    secret = "영구는 배꼽이 두 개다."

    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." %(self.name, a, b, result))

pey = Service1('Marcus')
pey.sum(4, 8)

# 출력 결과
Marcus님 4 + 8 = 12입니다.
</code></pre>

클래스 자세히 알기
------------------

클래스의 구조

<pre><code>
class 클래스 이름[(상속 클래스명)]:  
    <클래스 변수1>  
    <클래스 변수2>  
    <클래스 변수N>
      
    def 클래스 함수1(self, 인수1, 인수2, ...):  
        <수행할 문장1>  
        <수행할 문장2>
          
    def 클래스 함수2(self, 인수1, 인수2, ...):  
    <수행할 문장1>  
    <수행할 문장2>
</code></pre>

사칙연산 클래스 만들기
---------------------

<pre><code>
class FourCal:

    def setData(self, a, b):
        self.arg1 = a
        self.arg2 = b

    def sum(self):
        return self.arg1 + self.arg2

    def sub(self):
        return self.arg1 - self.arg2

    def mul(self):
        return self.arg1 * self.arg2

    def div(self):
        return self.arg1 / self.arg2

dev = FourCal()
dev.setData(4, 2)

print(dev.sum())
print(dev.sub())
print(dev.mul())
print(dev.div())

# 출력 결과
6
2
8
2.0
</code></pre>

'박씨네 집' 클래스 만들기
----------------------

<pre><code>
class HousePark:
    lastName = "박"

    def setName(self, name):
        self.fullName = self.lastName + name

    def travel(self, locaiton):
        print('%s, %s여행을 가다.' %(self.fullName, locaiton))

pey = HousePark()

pey.setName("기득")
print(pey.fullName)

pey.travel("일본")

# 출력 결과
박기득
박기득, 일본여행을 가다.
</code></pre>

초깃값 설정하기
---------------

<pre><code>
class initHousePark:
    lastName = "박"

    def __init__(self, name):
        self.fullName = self.lastName + name

    def travel(self, locaiton):
        print('%s, %s여행을 가다.' %(self.fullName, locaiton))

pey1 = initHousePark("기득")
print(pey1.fullName)

pey1.travel("홍대")

# 출력 결과
박기득
박기득, 홍대여행을 가다.
</code></pre>

클래스의 상속
-----------------

> class 상속받을 클래스명(상속할 클래스명):

<pre><code>
class houseShin(InitHousePark):
    lastName = "신"

shin = houseShin("재규")
print(shin.fullName)

shin.travel("헤화")

# 출력 결과
신재규
신재규, 헤화여행을 가다.
</code></pre>

메서드 오버라이딩

- 메서드 이름을 동일하게 다시 구현하는 것

<pre><code>
class HouseKim(InitHousePark):
    lastName = "김"

    def travel(self, locaiton, days):
        print("%s, %s여행 %d일 가네." %(self.fullName, locaiton, days))

kim = HouseKim("민지")
print(kim.fullName)

kim.travel("일본", 5)

# 출력 결과
김민지
김민지, 일본여행 5일 가네.
</code></pre>

연산자 오버로딩
------------------

<pre><code>
class InitHousePark:
    lastName = "박"

    def __init__(self, name):
        self.fullName = self.lastName + name

    def travel(self, locaiton):
        print('%s, %s여행을 가다.' %(self.fullName, locaiton))

    def love(self, other):
        print("%s, %s 사랑에 빠졌네" %(self.fullName, other.fullName))

    def __add__(self, other): # 연산자 오버로딩 사용
        print("%s, %s 결혼했네" %(self.fullName, other.fullName))
        
class HouseKim(InitHousePark):
    lastName = "김"

    def travel(self, locaiton, days):
        print("%s, %s여행 %d일 가네." %(self.fullName, locaiton, days))

p = InitHousePark("사랑")
k = HouseKim("우정")

p.love(k)
p + k

# 출력 결과
박사랑, 김우정 사랑에 빠졌네
박사랑, 김우정 결혼했네
</code></pre>

<pre><code>
class InitHousePark:
    lastName = "박"

    def __init__(self, name):
        self.fullName = self.lastName + name

    def travel(self, locaiton):
        print('%s, %s여행을 가다.' %(self.fullName, locaiton))

    def love(self, other):
        print("%s, %s 사랑에 빠졌네" %(self.fullName, other.fullName))

    def __add__(self, other):
        print("%s, %s 결혼했네" %(self.fullName, other.fullName))

    def fight(self, other):
        print("%s, %s 싸우네" %(self.fullName, other.fullName))

    def __sub__(self, other):
        print("%s, %s 화해하네" %(self.fullName, other.fullName))

        
class HouseKim(InitHousePark):
    lastName = "김"

    def travel(self, locaiton, days):
        print("%s, %s여행 %d일 가네." %(self.fullName, locaiton, days))

p = InitHousePark("사랑")
k = HouseKim("우정")

p.travel("일본")
k.travel("일본", 3)
p.love(k)
p + k
p.fight(k)
p - k

# 출력 결과
박사랑, 일본여행을 가다.
김우정, 일본여행 3일 가네.
박사랑, 김우정 사랑에 빠졌네
박사랑, 김우정 결혼했네
박사랑, 김우정 싸우네
박사랑, 김우정 화해하네
</code></pre>




