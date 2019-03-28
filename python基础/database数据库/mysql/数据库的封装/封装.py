# coding=utf-8
from MysqlHelper import MysqlHelper


def testMyhelper():
    name = input("请输入学生姓名：")
    sex = input("请输入学生性别：")
    age = input("请输入学生年龄：")
    income = input("请输入学生收入：")
    myselHelper = MysqlHelper("localhost", 3306, "python3", "root", "yyh123", "utf8")
    # myselHelper = MysqlHelper("localhost","python3","root","yyh123","utf8")
    sql = "insert into mytest(name,sex,age,income)values (%s,%s,%s,%s)" % (
    "'" + name + "'", "'" + sex + "'", age, income)
    myselHelper.cud(sql)


def testMyhelper2():
    name = input("请输入学生姓名：")
    sex = input("请输入学生性别：")
    age = input("请输入学生年龄：")
    income = input("请输入学生收入：")
    myselHelper = MysqlHelper("localhost", 3306, "python3", "root", "yyh123", "utf8")
    # myselHelper = MysqlHelper("localhost","python3","root","yyh123","utf8")
    sql = "insert into mytest(name,sex,age,income)values (%s,%s,%s,%s)";
    params=[name,sex,age,income]
    myselHelper.cudWithParams(sql,params)


def queryStudentData():
    pass
    sql = "select name ,sex,age ,income from mytest where income > %s"
    sql2 = "select name ,sex,age ,income from mytest where income > 5000"
    mysqlHelper = MysqlHelper("localhost", 3306, "python3", "root", "yyh123", "utf8")
    result = mysqlHelper.queryAll(sql,1000)
    print(result)

maxn = 10001
dp = [maxn]
def main():
    num = {5, 10, 20, 50, 100}
    for i in range(maxn):
        dp.append(1)
    for i in range(maxn):
        # ss = num[i]
        for j in range(i):
            # for(j = num[i]; j < maxn; ++j)
            result = dp[j] + dp[j - num[i]]
            # dp[j] += dp[j - num[i]];
            dp[j] = result
            print("%lld" % dp[maxn - 1]);
        return 0;


if __name__ == "__main__":
    pass
    # testMyhelper()
    # testMyhelper2()
    queryStudentData()
    # main()
