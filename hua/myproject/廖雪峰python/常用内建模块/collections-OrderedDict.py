#使用dict时，Key是无序的。在对dict做迭代时，我们无法确定Key的顺序。
#如果要保持Key的顺序，可以用OrderedDict：
from collections import OrderedDict
d=dict([('a',1),('c',3),('b',2)])
print(d)#dict的key是无序的
od=OrderedDict([('b', 2),('a', 1), ('c', 3)])
print(od)# OrderedDict的Key是有序的
#OrderedDict的Key会按照插入的顺序排列，不是Key本身排序：
d=dict()
d['z']=1
d['y']=2
d['x']=3
list(d.keys())

