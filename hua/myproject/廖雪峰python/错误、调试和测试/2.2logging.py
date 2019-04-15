#把print()替换为logging是第3种方式，和assert比，logging不会抛出错误，而且可以输出到文件
import logging
logging.basicConfig(level=logging.INFO)
s= '0'
n = int(s)
logging.info('n=%d'% n)#logging.info()就可以输出一段文本。
print(10/n)






