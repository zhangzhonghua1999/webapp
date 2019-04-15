#Python的dict对象可以直接序列化为JSON的{}，
# 不过，很多时候，我们更喜欢用class表示对象，比如定义Student类，然后序列化：

import json
class Student(object):
    def __init__(self,name,age,score):
        self.name=name
        self.age=age
        self.score=score

s=Student('zzh',20,100)
def student2dict(std):
    return {
        'name':std.name,
        'age':std.age,
        'score':std.score
    }

#print(json.dumps(s,default=student2dict))
print(json.dumps(s,default=lambda obj: obj.__dict__))#偷懒写法

#如果我们要把JSON反序列化为一个Student对象实例，loads()方法首先转换出一个dict对象，
# 然后，我们传入的object_hook函数负责把dict转换为Student实例：
def dict2student(d):
    return Student(d['name'],d['age'],d['score'])

json_str = '{"age": 20, "score": 88, "name": "Bob"}'
print(json.loads(json_str, object_hook=dict2student))


