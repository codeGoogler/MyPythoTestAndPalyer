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
def colseCursor(cursor):
    cursor.close()

def createTable(db):
    try:
        cursor = db.cursor()
        cursor.execute("drop table if exists MyTest")
        sql = "create table MyTest(" \
              "id int primary key auto_increment not  null ," \
              "name varchar(20)," \
              "age int ," \
              "sex varchar(10), " \
              "income float" \
              ")"
        i = cursor.execute(sql)
        print(i)
        colseCursor(cursor)
    except  Exception as e:
        print(e)


def insertValuesToTable(db):
    try:
        cursor = db.cursor()
        for i in range(10):
            name = "卡卡罗特"+str(i)
            age = random.randint(20,100)
            if 1 %2 == 0:
                sex = "赛亚人"
            else:
                sex = "普通人"
            income = random.uniform(2000,10000)
            mysql = "insert into MyTest(name,age,sex,income)values('%s',%s,'%s','%s')"%(name,str(age),str(sex),str(income))
            #  mysql = "insert into MyTest(name,age,sex,income)values('%s',%s,'%s','%s')"%("卡卡罗特","1","12","12")
            cursor.execute(mysql)
        db.commit()
        colseCursor(cursor)
    except Exception as e:
        print(e)
        db.rollback()


def queryAllData(db):
    try:
        cursor = db.cursor()
        sql = "select * from MyTest where age >25"
        cursor.execute(sql)

        result = cursor.fetchall()
        print(result)

        for sudent in result:
            print(sudent)

        colseCursor(cursor)
    except Exception as  e:
        print(e)

def queryAllData2(db):
    try:
        cursor = db.cursor()
        sql = "select * from MyTest where age >%d and income >%ld"%(50,8000)
        cursor.execute(sql)

        result = cursor.fetchall()
        print(result)

        for sudent in result:
            print(sudent)
        colseCursor(cursor)
    except Exception as  e:
        print(e)
        import traceback
        traceback.print_exc()



def updateOneMoeThing(db):
    name1 = '"kklt"'
    try:
        cursor = db.cursor()
        sql = "update MyTest set income=%s, name=%s where age>%d"%(5000,name1,50)
        # sql = "update MyTest set income=%d where age>%d"%(500000,50)
        result = cursor.execute(sql)
        db.commit()
        print(result)
        if result > 0:
            print("更改成功啦")
        else:
            print("更改失败")
        colseCursor(cursor)
    except Exception as e:
        print(e)
        db.rollback()


def deleteFormMorethan(db):
    name1 = '"kklt"'
    try:
        cursor = db.cursor()
        sql = "delete from MyTest where age >%d or name = %s"%(50,name1)
        # sql = "update MyTest set income=%d where age>%d"%(500000,50)
        result = cursor.execute(sql)
        if result > 0:
            print("更改成功啦")
        else:
            print("更改失败")
        db.commit()
        colseCursor(cursor)
    except Exception as e:
        print(e)


def deleteFormMorethan2(db):
    try:
        cursor = db.cursor()
        sql = "delete from MyTest"
        # sql = "update MyTest set income=%d where age>%d"%(500000,50)
        result = cursor.execute(sql)
        if result > 0:
            print("清空表中数据")
        else:
            print("清空失败")
        db.commit()
        colseCursor(cursor)
    except Exception as e:
        print(e)


def trunctTable(db):
    try:
        cursor = db.cursor()
        sql = "truncate table MyTest"
        # sql = "update MyTest set income=%d where age>%d"%(500000,50)
        result = cursor.execute(sql)
        db.commit()
        if result > 0:
            print("表已删除")
        else:
            print("表已删除失败")
        colseCursor(cursor)
    except Exception as e:
        print(e)


def _testConnectDb():
    # 打开数据库
    db = pymysql.connect("localhost","root","yyh123","python3")

    #  适应cursor方法来回欧式操作的游标
    cursor = db.cursor()
    name = input("请输入你要添加名字：")
    age = input("请输入年龄：")
    sex = input("请输入性别：")
    income = input("请输入学生的薪水：")
    if name is not None:
        sql = "insert into MyTest(name,age,sex,income) values (%s,%s,%s,%s)"
        cursor.execute(sql,[name,age,sex,income])
        db.commit()
        print("插入成功~~")
        pass
    else:
        db.rollback()
        print("输入不能为空字符串")
        pass


if __name__ == "__main__":
    pass
    db = connectMySql()
    createTable(db)
    insertValuesToTable(db)
    # queryAllData(db)
    queryAllData2(db)
    #更改
    updateOneMoeThing(db)
    #删除表中的指定的一列
    deleteFormMorethan(db)
    #清空表
    deleteFormMorethan2(db)

    insertValuesToTable(db)

    # 删除表
    trunctTable(db)
    # 关掉游标，db，
    # 最后需要关掉数据库
    db.close()
    
    # 参数化
    _testConnectDb()

