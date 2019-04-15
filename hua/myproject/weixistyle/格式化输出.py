priceadult=270
pricechild=150

print('成人票价为:%d, 小孩票价为:%d' % (priceadult,pricechild))
adult=int(input('成人人数'))

child=int(input('小孩人数'))

total=adult*priceadult + child*pricechild

total=total*0.95

discount='95%'
print('当折扣为%s时,总票价为:%.2f' % (discount,total))