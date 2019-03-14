import os


def test01():
    try:
        test02()
        ss = open("E:\\Test.txt1", "w1")
        ss.write("你和我")

        isExist = os.path.exists("E:\\Test.txt")
        print(isExist)

    except FileExistsError:
        print("文件出错啦，hahhahah ")

    except Exception as ret:
        print(ret)
    finally:
        print("---------------------finally-------------------------")


def test02():
    try:

        i = 100;
        j = 0
        raise MyCatException("卡卡罗特", 100)
        ss = i / j
        print(ss)
    except MyCatException as  result:
        print(result.__str__())



# 自定义异常
class MyCatException(Exception):

    def __init__(self, exceptoionName, numType):
        self.exceptoionName = exceptoionName
        self.numType = numType

    def __str__(self):
        msg = "要抛出异常啦~~，类型名称为：%s ,y异常类型为： %d"%(self.exceptoionName, self.numType)
        return msg




#自定义异常 需要继承Exception

class MyException(Exception):

    def __init__(self, *args):
        self.args = args

#raise MyException('爆出异常吧哈哈')

#常见做法定义异常基类,然后在派生不同类型的异常

class loginError(MyException):
    def __init__(self, code = 100, message = '登录异常', args = ('登录异常',)):
        self.args = args
        self.message = message
        self.code = code
class loginoutError(MyException):
    def __init__(self):
        self.args = ('退出异常',)
        self.message = '退出异常'
        self.code = 200
#raise loginError() # 这里突然返现 raise引发的异常将中断程序
#
def test03():
    try:
        raise loginError()
    except loginError as e:
        print(e) #输出异常
        print(e.code) #输出错误代码
        print(e.message)#输出错误信息


def test04():
    try:
        raise loginError()
    except loginError as e:
        print(e) #输出异常
        print(e.code) #输出错误代码
        print(e.message)#输出错误信息
        i = 100;
        j = 0
        ss = i / j
        raise


if __name__ == "__main__":
    print("主函数走起~~")
    test02()
    test03()
    test04()
