

# 和set相比， 主要是有序 ,y不重复
import redis

r = redis.Redis(host="localhost", port=6379, db=0, password=None)

def test1():

    r.delete("2")
    r.sadd("2",1)
    r.sadd("2",2)
    r.sadd("2",3)
    r.sadd("2",4)
    r.sadd("2",5)
    r.sadd("2",5,6,7,8,9,0)

    print(r.sinter(2))

if __name__ == "__main__":
    pass
    test1()
