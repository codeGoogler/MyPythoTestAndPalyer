# coding=utf-8
from MysqlHelper import MysqlHelper


def testMyhelper():
    name = input("请输入学生姓名：")
    sex = input("请输入学生性别：")
    age = input("请输入学生年龄：")
    income = input("请输入学生收入：")
    myselHelper = MysqlHelper("localhost","7381","python3","root","yyh123","utf8")
    sql = "insert into mytest(name,sex,age,income)values (%s,%s,%s,%s)"
    myselHelper.cud(sql)

if __name__ == "__main__":
    pass
    testMyhelper()