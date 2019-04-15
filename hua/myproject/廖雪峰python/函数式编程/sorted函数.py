print(sorted([-1,3,-4,5,-20,8]))

print(sorted([-1,3,-4,5,-20,8],key=abs))

print(sorted(['bob','alice','Zoo'],key=str.lower))

print(sorted(['bob','alice','Zoo'],key=str.lower,reverse=True))

L=[('Bob',75),('Adam',92),('Bart',66),('Lisa',88)]

#按名字排序
def by_name(t):
    return t[0]
L2 = sorted(L, key=by_name)
print(L2)
#按成绩排序
def by_score(t):
    return t[1]
L3=sorted(L,key=by_score)
print(L3)






