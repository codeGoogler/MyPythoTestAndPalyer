import redis

r = redis.Redis(host="localhost", port=6379, db=0, password=None)



# hget(name,key)
# 在name 对应的hash 中设备键值对
# hset(name, key, value)
# 在name对应的hash中批量设置键值对

def test2():
    # 在name 对应的hash 中设备键值对
    r.hset( "Student","name","zhangsan")
    r.hset( "Student","age",13)
    r.hset( "Student","sex1","男")


    # 获取name对应hash的所有键值
    print( r.hgetall("Student"))

    # 在name对应的hash中获取根据key获取value
    print( r.hget("Student","name"))

    # 在name对应的hash中批量设置键值对
    r.hmset("Student",{"l1":"v1","l2":12,"l3":"v3"})

    # 在name对应的hash中获取多个key的值
    print(r.hmget("Student",{"l1","l2","l3"}))

    # 获取name对应的hash中键值的个数
    print(r.hlen("Student"))

    # 获取name对应的hash中所有的value的值
    print(r.hkeys("Student"))
    # print(r.keys("Student",))

    # 检查name对应的hash是否存在当前传入的key
    print(r.hexists("Student","aa"))
    print(r.hexists("Student","name"))

    # 删除hash'中指定的键值
    print(r.hdel("Student","l1","l2"))
    print(r.hdel("Student","l1"))

    r.hmset("Student",{"l1":"v1","l2":12,"l3":"v3"})
    #  Keys 命令用于查找所有符合给定模式 pattern 的 key 。
    print(r.keys(pattern="l*"))

def ss(*args):
    print(type(args))
    print(args)

if __name__ == "__main__":
    pass

    test2()
    # ss("1","2","3")

