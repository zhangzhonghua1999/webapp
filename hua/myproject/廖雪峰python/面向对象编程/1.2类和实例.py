class Students(object):
    def __init__(self,name,score):
        self.name = name
        self.score = score

    def print_score(self):
        print('%s:%s' % (self.name,self.score))

    def get_grade(self):
        if self.score >=90:
            return 'A'
        elif self.score >=60:
            return 'B'
        else:
            return 'C'


print(Students)
bart=Students('Bart ',99)
print(bart.name,bart.get_grade())
print(bart.score)

bart.print_score()

bart.age=8
print(bart.age)




