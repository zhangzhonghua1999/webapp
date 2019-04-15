#列出2-100之间的素数
'''
number=2

while (number<=100):
    i=2
    while (i<=(number-1)):
        if (number % i )==0:
            break
        i=i+1
    if i==number:
        print('%d 是素数' % number)
    number+=1
'''
#定义第一行
row =1
while row <=9:
    # 定义第一列
    col=1
    while col<=row:
        print('%d * %d = %d' % (col,row,col*row), end='\t')
        col+=1
    print('')
    row+=1




