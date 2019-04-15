class Students(object):

    def __init__(self,name,score):
        self.__name=name #在前面加个__可以禁止外部代码修改对象内部的状态
        self.__score=score

    def print_score(self):
        print('%s:%s' % (self.__name,self.__score))

    def set_score(self,score):
        if 0<=score <=100:
            self.__score=score
        else:
            raise ValueError('bad score')


bart=Students('Bart ',59)

bart.set_score(50)

bart.print_score()