# coding=utf-8

from MysqlHelper import MysqlHelper
from 与python进行交互 import ReadOrWriteUtilCall

from hashlib import sha1


def test():
    name = input("请输入用户名：")
    password = input("请输入密码：")

    if len(name) == 0:
        print("用户名不能为空")
        return
    if len(password) == 0:
        print("密码不能为空")
        return
    elif len(password) < 3:
        print("密码不能少于6位")
        return

    sha = sha1()
    sha.update(password.encode("utf8"))

    newpassword = sha.hexdigest()
    print("新密码加密：%s" % newpassword)
    r = ReadOrWriteUtilCall(host="127.0.0.1", port="6379", password="yyh123456")
    # sqlHelper = MysqlHelper(host="localhost",port="root" ,db = "python3",  password="root",charset="utf8")
    sqlHelper = MysqlHelper("localhost", 3306, "python3", "root", "yyh123", "utf8")
    # 首先判断redis缓存中有没有该条数据(此用户和密码)
    if r.read(name) == None:
        sql = "select password from user where name = %s"
        pwd = sqlHelper.queryOne(sql, [name])
        print(pwd)
        if pwd == None:
            print("用户名输入错误，请重新输入~")
            return
        else:  # 说明查到了数据
            # 然后把查出来的数据存到redis里面去
            print("redis中并没有这些数据~~")
            print(type(pwd[0]))
            r.save(name, pwd[0])
            if pwd[0] == newpassword:
                print("恭喜用户 ：%s ，登录成功" % (name))
            else:
                print("对不起吗，您的额密码输入有误，请重试...")
                return
    else:
        password = r.read(name)
        print(type(password))
        print(type(newpassword))
        print("password:%s"%password)
        print("password:%d,   newpassword:%d"%(len(password),len(newpassword)))
        if str(password) == str(newpassword):
            print("恭喜用户 ：%s ，登录成功,嘎嘎" % (name))
        else:
            print("对不起吗，您的额密码输入有误，嘎嘎 请重试...")


if __name__ == "__main__":
    test()
