# class 변수

# class Service:
#     secret = "영구는 배꼽이 두 개다."
#
# pey = Service()
#
# print(pey.secret)

# class 함수

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

# __init__

class Service1:
    secret = "영구는 배꼽이 두 개다."

    def __init__(self, name):
        self.name = name

    def sum(self, a, b):
        result = a + b
        print("%s님 %s + %s = %s입니다." %(self.name, a, b, result))

pey = Service1('Marcus')
pey.sum(4, 8)

# 사칙연산

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

# 박씨네 집

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

# 박씨네 집 초깃값

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

pey1 = InitHousePark("기득")
print(pey1.fullName)

pey1.travel("홍대")

# 상속

class HouseShin(InitHousePark):
    lastName = "신"

shin = HouseShin("재규")
print(shin.fullName)

shin.travel("헤화")

# 메서드 오버라이딩

class HouseKim(InitHousePark):
    lastName = "김"

    def travel(self, locaiton, days):
        print("%s, %s여행 %d일 가네." %(self.fullName, locaiton, days))

kim = HouseKim("민지")
print(kim.fullName)

kim.travel("일본", 5)

# 연산자 오버로딩

p = InitHousePark("사랑")
k = HouseKim("우정")

p.travel("일본")
k.travel("일본", 3)
p.love(k)
p + k
p.fight(k)
p - k
