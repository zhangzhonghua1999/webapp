print(int('125'))

print(int('125',base=8))

print(int('125',base=16))

'''
def int2(x,base=2):
    return int(x,base)

print(int2('100'))
'''


import functools
int2= functools.partial(int,base=2)

print(int2('100'))






