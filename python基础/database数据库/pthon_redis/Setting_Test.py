# coding=utf-8
import redis
"""redix python的学习博客：  https://www.cnblogs.com/baby123/p/7245086.html   
    https://www.cnblogs.com/lezhifang/p/7027903.html
    下载redis: https://github.com/MicrosoftArchive/redis/releases
    命令： http://www.redis.cn/commands.html 
    系列教程：https://www.cnblogs.com/xuchunlin/p/7061524.html
"""


def test1():
    # r=redis.Redis(host='127.0.0.1',port=6379,db=0)
    r=redis.Redis(host='127.0.0.1',port=6379,db=0,password="yyh123456")
    r.set('name','baby')
    print(r.get('name'))
    print(r.dbsize())
    print(r.time())
    r.set("name","于亚豪")
    r.set("age",29)
    r.set("sex","1")
    r.set("income",34.2)
    r.set("income",34.2)

    print(r.get("name"))
    print(r.get("age"))
    print(r.get("sex"))
    print(r.get("income"))

    print(r.dump("name"))

    print(r.delete("name","age","12"))
    print(r.exists("income","123"))


#
if __name__ == "__main__":
    pass
    test1()
    # redis 是属于key-values 的数据格式
    # key: string
    # value的类型
    #