class Students(object):
    def __init__(self,name,score):
        self.name= name
        self.score= score
    def print_score(self):
        print('%s: %s' % (self.name, self.score))

bart = Students('Bart Simpson', 59)
lisa = Students('Lisa Simpson',87)
bart.print_score()
lisa.print_score()

print(bart.name)
print(bart.score)


