# 추가하기

info = {'name':'marcus'}
info['birth'] = 1992

print(info)

# 삭제하기

info['no'] = 92

del info['birth']

print(info)

# value 얻기

print(info['name'])
print(info['no'])

info[1] = 'I'
info[2] = 'U'

print(info[1])
print(info[2])

# 중복 key

a = {1:'일', 1:'이'}

print(a[1])

# list in key

# a[[3, 4]] = '삼사'

# keys

print(info.keys())

# for keys

for k in info.keys():
    print(k)

# list로 변환

b = list(info.keys())

print(b)

# values

print(info.values())

# items

print(info.items())

# get

print(info.get('name'))
print(info.get('no'))
print(info.get('birth'))

# print(info['birth'])

print(info.get('birth', 1992))

# in

print('birth' in info)
print('name' in info)