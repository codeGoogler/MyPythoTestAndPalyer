import redis
from redis import Redis

r: Redis = redis.Redis(host="localhost", port=6379, db=0, password=None)


def test2():
    pass
    r.lpush("list", "1")
    r.lpush("list", 2)
    r.lpush("list", 3)
    r.lpush("list", "wo")
    r.lpush("list", "你")
    r.rpush("list", "她")

    print(r.lpop("list"))
    print(r.lpop("list"))
    print(r.lpop("list"))
    print(r.lpop("list"))
    print(r.rpop("list"))

    print(r.rpush("4", 1, 2, 3, 4, 5, 6, ))  # 输出的结果是6
    print(r.brpop("4"))  # 输出的结果是('4', '6')
    print(r.brpop("4"))  # 输出的结果是('4', '5')
    print(r.brpop("4"))  # 输出的结果是('4', '4')
    print(r.brpop("5", timeout=2))  # 因为键 4 不存在，所以2秒后输出的结果是None

    print(r.rpush("6", 1, 2, 3))  # 输出的结果是3
    print(r.lindex("6", 1))  # 输出的结果是2
    print(r.lindex("6", 2))  # 输出的结果是3
    print(r.lindex("6", 3))  # 输出的结果是None
    print(r.lindex("6", 4))  # 输出的结果是None
    print(r.lindex("6", -1))  # 输出的结果是3
    print(r.lrange("6", 1, 4))  # 控制的是范围

    print("*" * 50)
    """6. Lindex 命令用于通过索引获取列表中的元素。你也可以使用负数下标，以 -1 表示列表的最后一个元素， -2 表示列表的倒数第二个元素，以此类推。"""
    r.rpush("6",1,2,3,4,5,6,7,8,9,10)
    print(r.lindex("6",-1))
    print(r.lindex("6",-2))
    print(r.lindex("6",0))
    print(r.lindex("6",1))
    print(r.lindex("6",2))

    print("*" * 50)
    """7. Linsert 命令用于在列表的元素前或者后插入元素。"""
    r.linsert("6","BEFORE",1,0)
    # print(r.lrange("6",0,r.llen("6")-1))
    print(r.rpop("6"))
    print(r.lpop("6"))

    print("*" * 50)
    """9. Lpop 命令用于移除并返回列表的第一个元素。"""
    print(r.lpop("6"))
    print(r.lpop("6"))
    print(r.lpop("6"))
    print(r.lpop("6"))
    print(r.lpop("6"))
    print(r.lpop("6"))

    print("*" * 50)
    """10.Lpushx 将一个或多个值插入到已存在的列表头部，列表不存在时操作无效。"""
    print(r.lpushx("10",1))
    print(r.lpushx("10",2))
    print(r.lpush("10",6))
    print(r.lpush("10",7))
    print(r.lrange("10",0,-1))

    print("*" * 50)
    """13. Lset 通过索引来设置元素的值。"""
    print(r.rpush("131",12,3,4,5,6,7,8))
    print(r.lpushx("131",1))
    print(r.lset("131",1,2))
    print(r.lrange("131",0,-1))
    # print(r.l)

    print("*" * 50)
    """15. Rpop 命令用于移除并返回列表的最后一个元素。"""
    # print(r.rpush("15",1))
    # print(r.rpush("15",2,3,4,5,6))
    # print(r.rpop("15"))
    print(r.lrange("15",0,-1))

    print("*" * 15)
    """16.Rpoplpush 命令用于移除列表的最后一个元素，并将该元素添加到另一个列表并返回。"""
    print(r.rpush("16", 1, 2, 3, 4))  # 输出的结果是4
    print(r.rpush("17", 1, 2, 3, 4))  # 输出的结果是4
    print(r.rpoplpush("16", "17"))  # 输出的结果是4
    print(r.lrange("16", 0, -1))  # 输出的结果是['1', '2', '3']
    print(r.lrange("17", 0, -1))  # 输出的结果是['4', '1', '2', '3', '4']

    print("*" * 15)
    # print(r.rpush("18", 2))  # 输出的结果是1
    # print(r.rpushx("18", 1))  # 因为键18 不存在，所以插入失败，输出的结果是0
    # print(r.rpushx("18", 3))  # 输出的结果是2
    print(r.lrange("18", 0, -1))  # 输出的结果是['2', '3']
    print(r.rpush("18", 2))  # 输出的结果是1
    print(r.rpushx("18", 1))  # 因为键18 不存在，所以插入失败，输出的结果是0
    print(r.rpushx("18", 3))  # 输出的结果是2
    # 注意，这个是返回列表的长度


if __name__ == "__main__":
    pass
    test2()
