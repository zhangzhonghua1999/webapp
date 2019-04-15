#使用dict时，如果引用的Key不存在，就会抛出keyError。如果希望key不存在时，返回一个默认值，就可以用defaultdict：
from collections import defaultdict

d=defaultdict(lambda: 'N/A')#'N/A返回的默认值
d[1]='abc'
print(d[1])
print(d[2])#d[2]不存在，返回默认值
#注意默认值是调用函数返回的，而函数在创建defaultdict对象时传入。

