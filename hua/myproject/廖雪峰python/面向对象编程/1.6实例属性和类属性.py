class Student(object):
    def __init__(self,name):
        self.name=name

s= Student('bob')
s.score=90

# 类属性
class student(object):
    name= 'student'

s=student()#创建实例
print(s.name)
# 打印name属性，因为实例并没有name属性，所以会继续查找class的name属性

print(student.name)#打印类的name属性

s.name='zhangzhonghua'#给实例绑定name属性

print(s.name)#由于实例属性优先级比类属性高，因此，它会屏蔽掉类的name属性

print(student.name)# 但是类属性并未消失，用Student.name仍然可以访问

'''
del s.name # 如果删除实例的name属性

print(s.name)# 再次调用s.name，由于实例的name属性没有找到，类的name属性就显示出来了
'''



