# 1

def fib(n):
    if n == 0: return 0
    if n == 1: return 1
    return fib(n-1) + fib(n-2)

# 2

f = open("/Users/teddy/Desktop/sample.txt", "w")

A = [70, 60, 55, 75, 95, 90, 80, 80, 85, 100]

for i in A:
    data = "%d\n" %i
    f.write(data)

f.close()

f = open("/Users/teddy/Desktop/sample.txt", "r")
lines = f.readlines()
f.close()

total = 0

for line in lines:
    score = int(line)
    total += score

average = total / len(lines)

f = open("/Users/teddy/Desktop/result.txt", "w")
f.write('%d' %average)
f.close()