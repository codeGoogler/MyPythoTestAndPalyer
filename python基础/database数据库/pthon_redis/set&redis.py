import redis

r = redis.Redis(host="localhost", port=6379, db=0, password=None)


def test1():
    # r.delete("1")
    # print(r.sadd("1", 1))
    # print(r.sadd("1", 2))
    # print(r.sadd("1", 3))
    # print(r.sadd("1", 4))
    # print(r.sadd("1", 5))
    # print(r.sadd("1", 5,6,7,8,9,0,1,123))

    print(r.scard("1"))
    print(r.sinter("1"))
    print(r.smembers("1"))
    print(r.sismember("1",12))

if __name__ == "__main__":
    pass
    test1()
