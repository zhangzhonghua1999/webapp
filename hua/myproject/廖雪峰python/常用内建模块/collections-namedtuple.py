#collections是Python内建的一个集合模块，提供了许多有用的集合类。

#         namedtuple
#namedtuple是一个函数，它用来创建一个自定义的tuple对象，
# 并且规定了tuple元素的个数，并可以用属性而不是索引来引用tuple的某个元素。

from collections import namedtuple
# namedtuple('名称', [属性list]):

Point=namedtuple('Point',['x','y'])
P=Point(1,2)
print(P.x)
print(P.y)
print('---------------------------------------------------------')
#如果要用坐标和半径表示一个圆，也可以用namedtuple定义：
Circle=namedtuple('Circle',['x','y','r'])
























