#创建连接池
#我们需要创建一个全局的连接池，每个HTTP请求都可以从连接池中直接获取数据库连接。
#使用连接池的好处是不必频繁地打开和关闭数据库连接，而是能复用就尽量复用。
#连接池由全局变量__pool存储，缺省情况下将编码设置为utf8，自动提交事务。
import logging,asyncio,aiomysql

def log(sql,args=()):
    logging.info('SQL:%s' % sql)

async def create_pool(loop,**kw):
    logging.info('create database connection pool...')
    global __pool
    __pool=await aiomysql.create_pool(
        host=kw.get('host','localhost'),
        port=kw.get('port',3306),
        user=kw['user'],
        password=kw['password'],
        db=kw['db'],
        charset=kw.get('charset','utf-8'),
        autocommit=kw.get('autocommit',True),
        maxsize=kw.get('maxsize',10),
        minsize=kw.get('minsize',1),
        loop=loop
    )
#Slecet
#要执行SELECT语句，我们现用select函数执行，需要传入SQL语句和SQL参数。

async def select(sql,args,size=None):
    log(sql,args)
    global __pool
    with (await __pool) as conn:
        async with conn.cursor



























