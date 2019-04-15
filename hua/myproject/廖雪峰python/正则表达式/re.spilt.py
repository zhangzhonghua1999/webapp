'''
#split 方法按照能够匹配的子串将字符串分割后返回列表，它的使用形式如下：
re.split(pattern, string[, maxsplit=0, flags=0])
maxsplit  分隔次数，maxsplit=1 分隔一次，默认为 0，不限制次数。
'''

import re
r=re.split('[n]','runoob')
print(r)

print(re.split('\W+', 'runoob, runoob, runoob.'))
print('****************************************')
print(re.split('(\W+)', ' runoob, runoob, runoob.'))
print('****************************************')
print(re.split('\W+', ' runoob, runoob, runoob.', 1))
print('****************************************')

print(re.split('a', 'hello world')) # 对于一个找不到匹配的字符串而言，split 不会对其作出分割
