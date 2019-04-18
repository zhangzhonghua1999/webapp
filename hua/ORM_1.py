#创建一个Field类
class Field(object):

    def __init__(self,name,column_tye):
        self.name=name
        self.column_type=column_tye

    def __str__(self):
        return '<%s:%s>' % (self.__class__.__name__,self.name)
#作用是
#在Field类实例化时将得到两个参数，name和column_type，它们将被绑定为Field的私有属性，
# 如果要将Field转化为字符串时，将返回“Field:XXX” ， XXX是传入的name名称。

#创建StringField和IntergerField
#作用：在StringField,IntegerField实例初始化时，时自动调用父类的初始化方式。
class StringField(Field):
    def __init__(self,name):
        super(StringField,self).__init__(name,'varchar(100)')

class IntegerField(Field):
    def __init__(self,name):
        super(IntegerField,self).__init__(name,'bigint')

# 道生一：传入type
class ModelMetaclass(type):
    # 传入三大永恒命题：类名称、父类、属性
    def __new__(cls, name, bases, attrs):
        # 排除Model类本身：
        if name == 'Model':
            return type.__new__(cls,name,bases,attrs)
        print('Found model: %s' % name)
        mappings = dict()
        for k, v in attrs.items():
            if isinstance(v,Field):
                print('Found mapping: %s ==> %s ' % (k,v))
                mappings[k]=v
        for k in mappings.keys():
            attrs.pop(k)
        attrs['__mappings__'] = mappings # 保存属性和列的映射关系
        attrs['__table__'] = name        # 假设表名和类名一致
        return type.__new__(cls, name, bases, attrs)
'''
    它做了以下几件事

    创建一个新的字典mapping
    将每一个类的属性，通过.items()遍历其键值对。如果值是Field类，则打印键值，
并将这一对键值绑定到mapping字典上。
    将刚刚传入值为Field类的属性删除。
    创建一个专门的__mappings__属性，保存字典mapping。
    创建一个专门的__table__属性，保存传入的类的名称。
'''

#一生二
class Model(dict,metaclass=ModelMetaclass):

    def __init__(self,**kwarg):
        super(Model, self).__init__(**kwarg)

    def __getattr__(self, key):
        try:
            return self[key]
        except KeyError:
            raise AttributeError("'Model' object has no attribute '%s'" % key)

    def __setattr__(self, key, value):
        self[key] = value

    # 模拟建表操作
    def save(self):
        fields = []
        args = []
        for k, v in self.__mappings__.items():
            fields.append(v.name)
            args.append(getattr(self, k, None))
        sql = 'insert into %s (%s) values (%s)' % (self.__table__, ','.join(fields), ','.join([str(i) for i in args]))
        print('SQL: %s' % sql)
        print('ARGS: %s' % str(args))

class User(Model):
    # 定义类的属性到列的映射：
    id = IntegerField('id')
    name = StringField('username')
    email = StringField('email')
    password = StringField('password')


u = User(id=12345, name='Batman', email='batman@nasa.org', password='iamback')
u.save()