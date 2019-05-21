# 생성

s1 = set([1, 2, 3])
print(s1)

s2 = set("Hello world")
print(s2)

# 리스트로 변환

l1 = list(s1)

print(l1)

t1 = tuple(s1)

print(t1)

# 교집합

s3 = set([1, 3, 5, 2, 4, 6])
s4 = set([3, 5, 7, 2, 9, 0])

print(s3 & s4)
print(s3.intersection(s4))

# 합집합

print(s3 | s4)
print(s3.union(s4))

# 차집합

print(s3 - s4)
print(s3.difference(s4))

# add

s3.add(8)
print(s3)

# update

s3.update([11, 21, 31])
print(s3)

# remove

s3.remove(11)
print(s3)