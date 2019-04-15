class Animal(object):
    pass

# 大类:

class Mammal(Animal):
    pass

class Bird(Animal):
    pass

# 各种动物:
class Dog(Mammal):
    pass

class Bat(Mammal):
    pass

class Parrot(Bird):
    pass

class Ostrich(Bird):
    pass

class RunnableMixln(object):
    def run(self):
        print('running...')

class FlyableMixn(object):
    def fly(self):
        print('flying...')

class CarnivorousMixln(object):
    pass

class HerbivoresMixln(object):
    pass


#对于需要Runnable功能的动物，就多继承一个Runnable，例如Dog：
class Dog(Mammal,RunnableMixln):
    pass
#对于需要Flyable功能的动物，就多继承一个Flyable，例如Bat：
class Bat(Bird,FlyableMixln):
    pass


class Dog(Mammal,RunnableMixln,CarnivorousMixln):
    pass




