# 1

pin = '881120-1068234'
yyyymmdd = pin[:6]
num = pin[7:]

print(yyyymmdd)
print(num)

# 2

print(pin[7:8])

# 3

a = [1, 3, 5, 4, 2]
a.sort()
a.reverse()

print(a)

# 4

b = ['Life', 'is', 'too', 'short']
result = " ".join(b)

print(result)

# 5

c = 1, 2, 3
c = c + (4,)

print(c)

# 6

d = {'A':90, 'B':80, 'C':70}
result = d.pop('B')
print(d)
print(result)

# 7

e = [1, 1, 1, 2, 2, 3, 3, 3, 4, 4, 5]
eSet = set(e)
f = list(eSet)
print(f)

# 8

a = b = [1, 2, 3]
a[1] = 4
print(b)

# b를 출력하면 [1,, 4, 3]이 나온다. 이유는 a와 b가 같은 객체를 가리키고 있기 때문인데, 이를 방지하고자 한다면 copy 모듈을 사용하거나 [:]로 리스트를 따로 구성하면 된다.