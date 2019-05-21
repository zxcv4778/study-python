
# list 인덱싱

list = [1, 2, 3, 4, 'list', 'hello']

print(list[0] + list[3])
print(list[4] + list[5])
print(list[-1])

list1 = [2, 4, 5, ['twice', 'izone']]

print(list1[-1][0])
print(list1[-1][1])

# List 슬라이싱

print(list[:3])
print(list[3:])

# list +

listA = [1, 2, 3]
listB = [4, 5, 6]

print(listA + listB)

# list *

print(listA * 3)
print(listB * 3)

# change args

listA[1] = 9
listB[2] = 0

print(listA)
print(listB)

listA[1:2] = ['twice', 'izone']
listB[1] = ['once', 'wizone']

print(listA)
print(listB)

# delete args

listA[0:1] = []
print(listA)

listA[2:3] = []
print(listA)

del listB[0]
print(listB)

del listB[-1]
print(listB)

# append

twice = ['나연']
twice.append('사나')
twice.append('미나')
twice.append('지효')
twice.append('다현')

print(twice)

# sort

numbers = [8, 3, 2, 0]
numbers.sort()

print(numbers)

# reverse

twice.reverse()

print(twice)

# index

print(twice.index('사나'))
print(twice.index('나연'))

nationalAssembly = ['세금', '권력', '체면', '꼰대']

# print(nationalAssembly.index('상식'))

# insert

nationalAssembly.insert(0, '개판')

print(nationalAssembly)

# remove

nationalAssembly.remove('체면')

print(nationalAssembly)

# pop

print(nationalAssembly.pop(0))
print(nationalAssembly)

# count

print(twice.count('나연'))

# extend

twice.extend(['모모', '정연', '채영', '쯔위'])
print(twice)