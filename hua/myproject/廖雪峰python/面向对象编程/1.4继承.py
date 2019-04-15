class Zombie:

    def __init__(self,hp,dp):
        self.hp=hp
        self.dp=dp

    def gethp(self):
        if self.gethp>0:
            return self.hp
        else:
            return '已经挂掉'

    def getdp(self):
        return self.dp

    def bihit(self,lostpoint):
        self.hp -= lostpoint
        return lostpoint

class CommonZombie(Zombie):
    def wark(self):
        print('一大波僵尸正在接近')

class DropZombie(Zombie):
    def dropped(self):
        print('交通锥被打掉了')


Z1=CommonZombie(100,5)
Z2=DropZombie(200,10)


Z1.bihit(20)
Z2.bihit(11)

print(Z1.hp)
print(Z2.hp)

print(Z1.__dict__)




