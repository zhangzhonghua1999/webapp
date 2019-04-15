
priceadult=200
pricechild=100

print('成人票价为:',priceadult,'小孩票价为:',pricechild)
adult=int(input('成人人数'))
child=int(input('小孩人数'))
total=adult*priceadult + child*pricechild
'''
if total>0 and total<200:
    discount=1
else:
    if total>=200 and total<500:
        discount=0.95
    else:
        if total>=500 and total<1000:
            discount=0.9
        else:
            discount=0.8
'''
if total>0 and total<200:
    discount=1
elif total>=200 and total<500:
        discount=0.95
elif total>=500 and total<1000:
            discount=0.9
else:
    discount=0.8

print('原付：%d,应付：%.2f' % (total,total*discount))
