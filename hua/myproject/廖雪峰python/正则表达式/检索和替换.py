#Python 的re模块提供了re.sub用于替换字符串中的匹配项。
#re.sub(pattern,repl,string,count=0)
#pattern : 正则中的模式字符串。
#repl : 替换的字符串，也可为一个函数。
#string : 要被查找替换的原始字符串。
#count : 模式匹配后替换的最大次数，默认 0 表示替换所有的匹配。

import re
phone="199-7931-3119 # 这是一个电话号码"
#删除注释
num=re.sub(r'#.*',"",phone)
print('电话号码：',num)
#移除非数字的内容
num2=re.sub(r'-'," ",num)
print(num2)

num1=re.sub(r'\D','', phone)#\D非数字的字符
print('电话号码为%s' % num1)
