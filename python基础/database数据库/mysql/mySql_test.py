import random

import pymysql

# 学习案例


def connectMySql():
    # 打开数据库
    db = pymysql.connect("localhost","root","yyh123","python3")

    #  适应cursor方法来回欧式操作的游标
    cursor = db.cursor()

    # 查询当前数据库的版本
    cursor.execute("select version()")

    # 使用fetchone方法获取一条数据
    data = cursor.fetchone()

    var = "Database version : %s " % data
    print(var)

    # 用完数据库，一定要关闭
    # db.close()
    return  db

def createTable(db):
    try:
        cursor = db.cursor()
        cursor.execute("drop table if exists MyTest")
        sql = "create table MyTest(" \
              "id int primary key auto_increment not  null ,"\
              "name varchar(20)," \
              "age int ,"\
              "sex varchar(10), "\
              "income float"\
              ")"
        i = cursor.execute(sql)
        print(i)
    except  Exception as e:
        print(e)


def insertValuesToTable(db):
    try:
        cursor = db.cursor()
        # for i in range(10):
        name = "卡卡罗特"+1
        age = random.randint(20,100)
        print(type(age))
        if 1 %2 == 0:
            sex = "赛亚人"
        else:
            sex = "普通人"
            income = random.uniform(8000,10000)
            mysql = "insert into MyTest(name,age,sex,income)values('%s',%s,'%s','%d')"%("卡卡罗特",age,sex,income)
            cursor.execute(mysql)
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

if __name__ == "__main__":
    pass
    db = connectMySql()
    createTable(db)
    insertValuesToTable(db)