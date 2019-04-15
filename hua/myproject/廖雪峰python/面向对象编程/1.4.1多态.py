"""
多态
"""

class Zombie:
    '''所有僵尸类的父类'''
    def attack(self):
        pass

class CommonZombie(Zombie):
    def attack(self):
        print("普通僵尸啃植物！")

class GiantZombie(Zombie):
    def attack(self):
        print("巨人僵尸锤植物！")

class ClownZombie(Zombie):
    def attack(self):
        print("小丑僵尸爆炸！")

'''
统一调用一个方法名，但不同的僵尸对象有不同的攻击方法
'''
z1 = CommonZombie()
z3 = GiantZombie()
z4 = ClownZombie()
z5 = CommonZombie()

z1.attack()
z3.attack()
z4.attack()
z5.attack()

