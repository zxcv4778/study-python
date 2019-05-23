# -*- coding: utf-8 -*-

# sys 모듈로 입력 인수 직접 주기

import sys

# args = sys.argv[1:]
# for i in args:
#     print(i)

args = sys.argv[1:]
for i in args:
    if i == args[-1]:
        print(i.upper(), end='\n')
    else:
        print(i.upper(), end=' ')
