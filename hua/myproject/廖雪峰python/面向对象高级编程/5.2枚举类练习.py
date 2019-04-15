from enum import Enum

Gender= Enum('Gender',('Male','Famale'))

for name, member in Gender.__members__.items():
    print(name,member)
'''
class Gender(Enum):
    Male=0
    Famale=1
'''
class Student(object):
    def __init__(self,name,gender):
        self.name=name
        self.gender=gender


bart = Student('Bart', Gender.Male)
if bart.gender == Gender.Male:
    print('测试通过!')
else:
    print('测试失败!')




