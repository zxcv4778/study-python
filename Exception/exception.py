
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
except IndexError:
    pass
finally:
    print("The Final")

# 오류 회피하기

try:
    f = open("no file", 'r')
except FileNotFoundError:
    pass

# 오류 발생시키기

class Bird:
    def fly(self):
        raise NotImplementedError

class Eagle(Bird):
    pass

eagle = Eagle()
eagle.fly()