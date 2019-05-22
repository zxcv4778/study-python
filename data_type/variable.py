import sys

# 생성

a = 3
b = 5
c = 5

print(type(3))

twice, izone = 'once', 'wizone'
[once, wizone] = ['twice', 'izone']
t = i = 'girlgroup'

a, b = b, a

print(a)
print(b)

print(a is b)
print(b is c)

# getrefcount
d = 5
print(sys.getrefcount(5))

e = 5
print(sys.getrefcount(5))

f = 5
print(sys.getrefcount(5))

g = 5
print(sys.getrefcount(5))

# [:]

listA = [1, 2, 3]
listB = listA[:]

listA[1] = 4

print(listA)
print(listB)

# copy

from copy import copy

listC = copy(listA)
print(listA is listC)