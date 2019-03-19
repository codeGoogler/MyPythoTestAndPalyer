# coding=utf-8
import time
import os

path_basefile = "E:\\Student_text.txt"
list = []

Student = {
    "name":"",
    "age":0,
    "sex":"男"
}


def addStudent():
    name = input("请输入您要添加的学生姓名：")
    age = input("请输入您要添加的学生年龄：")
    sex = input("请输入您要添加的学生写别：")

    Student["name"] = name
    Student["age"] = age
    Student["sex"] = sex
    list.append(Student)
    print("您添加的学生的信息为：姓名：%s ,年龄：%s, 性别：%s"%(name,age,sex))


def queryAllStudent():
    # isExist = os.path.exists(path_basefile)
    # if not isExist:
    #     print("数据库不存在")
    # else:
    #     print("加载数据库拉")
    #     file = open(path_basefile)
    #     allContent = file.read(2014)
    #     print("=======================================%s"%allContent)

    if len(list) == 0:
        print("学生表中暂时没有学生信息，请录入您的学生信息")
        return
    index = 0
    for student in list:
        index+=1
        # print("第%d学生的信息为：姓名：%s ,年龄：%s, 性别：%s"%(index,student.values[0],student.values[1],student.values[2]))
        print(student)


def defOneManagee():
    #  name = input("请输入您要添加的学生姓名：")
    # print("您添加的学生的信息为：姓名：%s ,年龄：%s, 性别：%s"%(name,age,sex))
    if len(list) == 0:
        print("学生表中暂时没有学生信息，请录入您的学生信息")
        return
    result = list.pop()
    if result == 0:
        print("已删除一个一个学生")


def saveAllInfoToFile():
    if len(list) == 0:
        return
    try:
        file = open(path_basefile,"w+")
        file.write(str(list))
        file.flush()
        file.close()
    except FileExistsError as e1:
        print(e1)
    except Exception as e:
        print(e)


def findOneInfo():
    if len(list) == 0:
        return
    print(list)
    for temp in list:
        print(temp["name"])

def dealSutdentManager(inputType):
    try:
        type = int(inputType)
        if type == 1:
            print("查询所有的学生")
            queryAllStudent()
            pass
        elif type == 2:
            print("添加一个学生")
            addStudent()
            pass
        elif type ==3:
            print("删除一个学生")
            defOneManagee()
            pass
        elif type == 4:
            print("修改一个学生")
            pass
        elif type == 5:
            saveAllInfoToFile()
        elif type == 6:
            pass
        elif type == 7:
            findOneInfo()
        elif type == 8:
            print("已退出")

    except Exception as e:
        print(e)
        print("请输入正确的操作类型")

def load_infor():

    global list

    try:
        f = open(path_basefile)
        list = eval(f.read())
        f.close()
    except Exception:
        pass

if __name__ == "__main__":
    pass
    """欢迎使用名片管理系统"""
    print("正在初始化.....")
    time.sleep(1) # 休眠1秒
    print("初始化成功！")
    print("正在加载...")
    print("欢迎使用名片管理系统")
    load_infor()
    while True:
        tipMessage = "输入下面的格式进行相应的功能：" \
                     "输入：1 ，查询所有的学生" \
                     "输入：2 ，添加一个学生" \
                     "输入：3 ，删除一个学生" \
                     "输入：4 ，修改一个学生" \
                     "输入：5 ，保存所有信息到文件" \
                     "输入：6 ，查修改某个学生的信息" \
                     "输入：7 ，查询某个学生" \
                     "输入：8 ，推出该系统"
        print(tipMessage)
        inputType = input("请输入您想要操作的类型:")
        dealSutdentManager(inputType)
        if inputType == "8":
            break



class Student1:

    def __init__(self):


        def __del__(self):
            pass
