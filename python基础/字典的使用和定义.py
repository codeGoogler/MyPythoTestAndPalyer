


student = {
    "name" : "",
    "age" : 1,
     "imagUrl" : "",
}


studentList = []

if __name__ == "__main__":
    student["name"]= "李四"
    student["age"] = 13
    student["imagUrl"]= "F:/Python_pro/MyPythoTestAndPalyer/python基础/字典的使用和定义.py"
    print(student)
    print(student.get("name"))
    print(student.get("age"))
    print(student.get("imagUrl"))
    # student.update("age","卡卡罗特")
    student["name"] = "卡卡罗特"
    print(student)
    # student.update('classes':"sd")
    # student.update(b=2)  #也可以
    student.update({"b": 2,'classes':"sd"})
    print(student)

    print(student)
    keys = student.keys()
    print(keys)


    print("*************************欢迎进入学生管理系统**********************")
    print("正在初始化....")
    print("编号：1 查询所有学生")
    print("编号：2 增加一个学生信息")
    print("编号：3 删除一个学生信息")
    print("编号：4 修改一个学生名片")
    print("编号：5 退出")

    while(True):
        type = input("请输入您要管理学生系统的编号：")
        type = int(type)
        if type == 1:
            if len(studentList) == 0:
                print("暂无学习信息，请进行其他操作")
            for ss in studentList:
                print(ss)
            pass
        elif type == 2:
            studentName = input("请输入学生的名称：")
            newStudent = student
            newStudent["name"] = studentName
            studentAge = input("请输入学生的年龄：")
            newStudent["age"] = studentAge
            studentList.append(newStudent)
            print("您已添加学生姓名为%s,年龄为：%d 到系统中"%(studentName,int(studentAge)))
            pass
        elif type == 3:
            if len(studentList) == 0:
                print("暂无学习信息，请进行其他操作")
            else:
                studentList.pop(0)
                pass
            pass
        elif type == 4:
            if len(studentList) == 0:
                print("暂无学习信息，请进行其他操作")
            else:
                for ss in studentList:
                    print(ss)
                delName = input("请输入您要删除学生的姓名")
                i=0;
                for ss in studentList:
                     if delName == ss["name"]:
                         print("已删除系统中姓名为%s的学生信息"%delName)
                         studentList.remove(ss)
                         break
                     i+=0
                if i == len(studentList):
                    print("sorry ,您输入学生的姓名未在给学生管理系统中，请进行其他操作~")
                pass
        elif type == 5:
            break