
# abs

print(abs(3))
print(abs(-3))
print(abs(-1.2))

# all

print(all([1,2,3]))
print(all([0,1,2,3]))

# any

print(any([1,2,3]))
print(any([0,1,2,3]))

# chr

print(chr(48))
print(chr(97))

# dir

print(dir([1,2,3,4]))
print(dir({1:'4'}))

# divmod

print(divmod(7, 3))
print(divmod(1.3, 0.2))

# enumerate

for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)

# eval

print(eval('3 + 4'))
print(eval("'hi' + 'a'"))
print(eval('divmod(4, 3)'))

# filter

def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# hex

print(hex(234))
print(hex(255))

# id

a = 3
print(id(3))
print(id(a))

b = a
print(id(b))

# input

# c = input()
# print(c)
#
# d = input("Enter: ")
# print(d)

# int

print(int('3'))
print(int(3.4))

print(int('11', 2))

# isinstance

class Person: pass

ins = Person()
print(isinstance(ins, Person))

noins = 3
print(isinstance(noins, Person))

# lambda

sum = lambda a, b: a + b
print(sum(3, 4))

# len

print(len("python"))
print(len([1,2,3]))
print(len((1,'a')))

# list

print(list('python'))
print(list((1,2,3)))

# map

def two_times(x): return x * 2

print(list(map(two_times, [1,2,3,4])))

# max

print(max([1, 2, 3]))
print(max("python"))

# min

print(min([1, 2, 3, 4]))
print(min("python"))

# oct

print(oct(34))
print(oct(123))

# ord

print(ord('a'))
print(ord('0'))


# pow

print(pow(2, 4))
print(pow(3, 3))

# range

print(list(range(5)))
print(list(range(5, 10)))
print(list(range(1, 10, 2)))

# sorted

print(sorted([3, 1, 2]))
print(sorted(['a', 'c', 'b']))

# str

print(str(3))
print(str('hi'))
print(str('hi'.upper()))

# tuple

print(tuple("abc"))
print(tuple([1, 2, 3]))
print(tuple((1, 2, 3)))

# type

print(type("abc"))
print(type([]))
print(type(open("test", 'w')))

# zip

print(list(zip([1, 2, 3], [4, 5, 6])))
print(list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9])))
print(list(zip("abc", "def")))