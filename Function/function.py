# 생성

def sum(a, b):
    return a + b

a = 3
b = 5
c = sum(a, b)

print(c)

# 입력값이 있는 함수

def summer(a, b):
    return a + b

s = summer(a, b)

# 입력값이 없는 함수

def say():
    return 'Hi'

hi = say()

print(hi)

# 결과값이 없는 함수

def sum2(a,b):
    print("%d, %d의 합은 %d입니다." %(a, b, a+b))

sum2(3, 4)

# 입력값 결과값 둘 다 없는 함수

def say2():
    print('Hello world')

say2()

# 여러 개의 입력값을 받는 함수

def sum_many(*args):
    sum = 0
    for i in args:
        sum = sum + i

    return sum

result = sum_many(1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

print(result)

def sum_mul(choice, *args):
    if choice == 'sum':
        result = 0
        for i in args:
            result = result + i
    elif choice == "mul":
        result = 1
        for i in args:
            result = result * i

    return result

resultSum = sum_mul("sum", 1, 2, 3, 4, 5)
resultMul = sum_mul('mul', 1, 2, 3, 4, 5,)

print(resultSum)
print(resultMul)

# 함수의 결과값은 언제나 하나임

def sum_and_mul(a, b):
    return a + b, a * b

resultSM = sum_and_mul(3, 4)

print(resultSM)

# 입력 인수에 초깃값 미리 설정하기

def say_myself(name, old, man=True):
    print('나의 이름은 %s입니다.' %name)
    print('나이는 %d살 입니다.' %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself("marcus", 28)
say_myself('민지', 25, False)

# 초깃값이 앞에 올 때

def say_myself2(name, man=True, old):
    print('나의 이름은 %s입니다.' %name)
    print('나이는 %d살 입니다.' %old)
    if man:
        print("남자입니다.")
    else:
        print("여자입니다.")

say_myself2("marcus", 28)