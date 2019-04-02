# coding="utf-8"

from redis import *

r = StrictRedis(host="127.0.0.1", port="6379", password="yyh123456")


class ReadOrWriteUtilCall(object):

    def __init__(self, host="127.0.0.1", port="6379", password="yyh123456"):
        self.host = host
        self.port = port
        self.passwrod = password
        self.r = StrictRedis(host=self.host, port=self.port, password=self.passwrod,decode_responses=True)

    def save(self, key, value):
        self.r.set(key, value)

    def read(self, key):
        if self.r.exists(key):
            return self.r.get(key)
        else:
            return None


def test():
    pass
    pipeline = r.pipeline()
    pipeline.set("py1", "1111")
    pipeline.set("py2", "bbbb")
    # 执行写入
    pipeline.execute()
    # str = '\xe5\x8d\xa1\xe5\x8d\xa1\xe7\xbd\x97\xe7\x89\xb9'
    # print(str.encode('utf-8'))


# 数据消息的格式

def readKeyData():
    print(r.get("py1"))
    print(r.get("py2"))


def test2():
    readKeyData = ReadOrWriteUtilCall()
    readKeyData.save("py3", "bbb")
    readKeyData.save("py4", "cccc")


def readKeyData2():
    readKeyData = ReadOrWriteUtilCall()
    print(readKeyData.read("py1"))
    print(readKeyData.read("py2"))
    print(readKeyData.read("py3"))
    print(readKeyData.read("py4"))

if __name__ == "__main__":
    test2()
    readKeyData2()
