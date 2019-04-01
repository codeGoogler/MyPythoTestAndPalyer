# coding="utf-8"
import redis

r = redis.Redis(host="localhost", port=6379, db=0, password=None)


def test1():
    r.delete("python1")
    r.lpush("python1", "name1")
    r.lpush("python1", "name2")
    r.lpush("python1", "name3")
    r.lpush("python1", "name4")
    r.lpush("python1", "name5")
    r.lpush("python1", "name6")
    r.lpush("python1", "name7")
    r.lpush("python1", "name8")
    r.lpush("python1", "name9")
    r.lpush("python1", "name10")
    r.lpush("python1", "name10","name11","name12")

    print("*" * 150)
    print(r.lrange("python1", 0, -1))
    print("*" * 150)
    ss = r.ltrim("python1", 2, 5)
    print(r.lrange("python1", 0, -1))
    print(ss)


def test2():
    r.delete("python1")
    r.lpushx("python1", "name1")
    r.lpush("python1", "name2")
    r.lpush("python1", "name3")
    r.lpush("python1", "name4")
    r.lpush("python1", "name5")
    r.lpush("python1", "name6")
    r.lpush("python1", "name7")
    r.lpush("python1", "name8")
    r.lpush("python1", "name9")
    r.lpush("python1", "name10")
    r.lpush("python1", "name10","name11","name12")

    print("*" * 150)
    print(r.lrange("python1", 0, -1))
    print("*" * 150)
    ss = r.ltrim("python1", 2, 10)
    print(r.lrange("python1", 0, -1))
    print(ss)


if __name__ == "__main__":
    pass

    test2()
