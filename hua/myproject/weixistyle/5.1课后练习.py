'''
综合练习 - 石头剪刀布小游戏

需求：
1.玩家从控制台输入一个数字：1代表石头，2代表剪刀，3代表布；
2.电脑玩家生产一个随机数，随机数可能为1或2或3，同样，1代表石头，2代表剪刀，3代表布；
3.通过比价玩家和电脑玩家所提供的数字，按石头剪刀布的胜负规则，由程序判定胜负，
	胜负规则：
	石头		胜		剪刀
	剪刀		胜		布
	布		胜		石头

关于随机数：
1. 要使用随机数，必须先导入相关模块，方法是在程序的顶部写import语句引入，格式为：
import random

2. 生成随机整数的方法是调用模块中的randint方法，格式为：
random.randint(a, b)
其中a和b为整数，执行后可以随机得到a到b之间的一个整数，包含a和b也可能的得到。例如：

random.randint(10,99)  # 可获得随机数n，n是10到99之间任一整数
'''

#要使用随机数生成的工具包，必须在文件的顶部引入
#import random

#1.玩家从控制台输入一个数字：1代表石头，2代表剪刀，3代表布；
player=int(input('玩家请输入一个数字，1=石头，2=剪刀，3=布'))
if player==1:
    strofplayer='石头'
elif player==2:
    strofplayer='剪刀'
else:
    strofplayer='布'

import random
computer=random.randint(1,3)
if computer==1:
    strofcomputer='石头'
elif computer==2:
    strofcomputer='剪刀'
else:
    strofcomputer='布'

print('这局玩家出的是%s,电脑出的是%s' % (strofplayer,strofcomputer))

if ((player==1 and computer==2)or(player==2 and computer==3)or(player==3 and computer==1)):
    print('玩家获胜')
elif ((player==1 and computer==3)or(player==3 and computer==2)or(player==2 and computer==1)):
    print('电脑获胜')
else:
    print('平局')
