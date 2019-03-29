# coding="utf-8"
import redis

r = redis.Redis(host="localhost", port=6379, db=0, password=None)


def test2():
    pass
    print(r.set('getrange', 'wo shi hao ren '))
    print(r.getrange('getrange', 2, 4))  # 返回的结果是sh
    print(r.getrange('getrange', 2, 6))  # 返回的结果是shi
    print(r.getrange('getrange', 2, 10))  # 返回的结果是shi hao

    r.set("name", "于亚豪")
    print(r.getrange("name", 0, 1))
    print(r.getset('getrange', 'hello word'))  # 返回的结果是wo shi hao ren
    print(r.getset('getrange11', 'hello word'))  # 当键不存在的时候，返回的结果是None
    
    # print(r.delete("getrange"))
    print(r.ttl("getrange"))
if __name__ == "__main__":
    pass

    test2()
