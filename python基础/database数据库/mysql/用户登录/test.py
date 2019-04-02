# coding=utf-8
import pymysql
from hashlib import sha1
from MysqlHelper import MysqlHelper

"""解密和解密参考： http://www.cnblogs.com/yyds/p/7072492.html"""

shaEncoding = sha1()
def encodingPass():
    pass
    # 需要加密的字符串
    pwd = "123"
    # 创建sha1对象
    s1 = sha1()
    # 对s1进行更新
    s1.update(pwd.encode())
    # 加密处理
    result = s1.hexdigest()
    # 结果是40位字符串：'40bd001563085fc35165329ea1ff5c5ecbdbbeef'
    print(result)


def testDb():
    pass
    # 打开数据库
    db = pymysql.connect("localhost", "root", "yyh123", "python3")

    #  适应cursor方法来回欧式操作的游标
    cursor = db.cursor()
    delSql = "drop table if exists user"
    cursor.execute(delSql)
    sql = "create table if not exists user(" \
          "id int  primary key  auto_increment not null," \
          "name varchar(20)," \
          "password char(40)" \
          ")"
    cursor.execute(sql)


def insertll():
    pymysqlHelper = MysqlHelper("localhost", 3306, "python3", "root", "yyh123", "utf8")
    for i in range(10):
        sa = sha1()
        if i == 6:
            sa.update(("12345" + str(i)).encode())
            password = sa.hexdigest()
            params = ["yyh" , password]
        else:
            sa.update(("12345" + str(i)).encode())
            password = sa.hexdigest()
            params = ["卡卡罗特" + str(i), password]
        sql = "insert into user (name ,password) values (%s,%s)"
        pymysqlHelper.cud(sql, params)


def login():
    name = input("请输入账户名：")
    password = input("请输入密码：")
    if len(name) == 0:
        print("请输入您的账号...")
        return
    elif len(password) < 6:
        print("密码长度不够...")
        return
    pymysqlHelper = MysqlHelper("localhost", 3306, "python3", "root", "yyh123", "utf8")
    sql = "select name,password from user where name = %s"
    result = pymysqlHelper.queryAll(sql, [name])
    try:
        if result is not None:
            isPass = 0
            for user in result:
                pas = shaEncoding.update(password.encode())
                passwprd  = shaEncoding.hexdigest()
                print( user[0])
                print( user[1])
                if user[0] == name and user[1] == passwprd:
                    print("登录成功")
                    print("恭喜 %s welcome to come!" % user[0])
                    isPass = 1
                    break

            if isPass == 0:
                print("用户名或者密码有误~~")
    except Exception as e:
        print(e)
    # print(result)


if __name__ == "__main__":
    pass
    # encodingPass()
    testDb();
    insertll()
    login()
