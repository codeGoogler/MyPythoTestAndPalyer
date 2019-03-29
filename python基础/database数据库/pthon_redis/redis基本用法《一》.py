import redis
from redis import Redis

r: Redis = redis.Redis(host="localhost", port=6379, db=0, password=None)


def test1():
    pass
    r.set("name", "yyh")
    r.set("name1", "yyh1")
    r.set("name2", "yyh2")
    r.set("name3", "yyh3")
    r.set("name4", "yyh4")
    r.set("age", 12)
    r.set("sex", "男")
    r.sadd("na",1)
    r.sadd("na",2)
    r.sadd("na",3)
    r.sadd("na",4)
    print(r.get("name"))
    print(r.get("age"))
    print(r.get("sex"))

    print(r.get("name"))
    print(r.exists("name"))
    print(r.exists("name1"))
    print(r.expire("name", 10))
    print(r.keys("name"))
    print(r.type("name"))
    print(r.type("age"))
    print(r.sinter("na"))
    print(r.type("na") == "b'set'")

    print(r.rename("name","yyhname"))
    print(r.exists("name"))
    print(r.exists("yyhname"))


    # 返回 key 的数据类型，数据类型有：none (key不存在)，string (字符串)，list (列表)，set (集合)，zset (有序集)，hash (哈希表)，
    print(r.set('1', "111111111"))
    print(r.type('1'))  # 返回的结果是string

    print(r.sadd('2', '222222222222'))
    print(r.type('2'))  # 返回的结果是set

    print(r.lpush('3', '33333333'))
    print(r.type('3'))  # 返回的结果是list

    print(r.set('111', '11'))
    print(r.set('122', '12'))
    print(r.set('113', '13'))
    print(r.keys(pattern='11*'))

def test2():
    pass
    print(r.exists("exists"))
    print(r.get("name"))

if __name__ == "__main__":
    pass
    test1()
    # test2()


    # redis 是属于key-values 的数据格式
    # key: string
    # value的类型
    #
