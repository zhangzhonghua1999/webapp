#一个网站应用运行时都需要读取配置文件，一般包括数据库的用户名、口令等。默认的配置文件应该符合本地开发环境，
# 我们把默认的配置文件命名为config_default.py:
configs = {
    'debug':True,
    'db':{
        'host':'127.0.0.1',
        'port':3306,
        'user':'www-data',
        'password':'www-data',
        'db':'awesome'
    },
    'session':{
        'secret':'Awesome'
    }
}