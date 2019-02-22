# coding=utf-8

def test():
    name= input("请输入您的年龄：")
    print("年龄：%s"%name)

def studySystem():
    print("***********************************欢迎进入填写学生系统************************************")
    name =input("请填写您的姓名：")
    print("您的姓名为：%s"%name)
    age = input("请填写您的年龄：")
    print("您的年龄为：%d",age)
    tel = input("请填写您的手机号")
    print("您的手机号为：%ld",tel)

    isCom = 1
    while isCom ==1 :
        print("正在检测中...")
        print("正在检测中...")
        print("正在检测中...")
        print("正在检测中...")
        print("正在检测中...")
        isCom = 2
        break
    print("恭喜姓名为：%s ， 手机号为%ld的同学录取成功"%name,"年龄为：%d"%age," 手机号为%ld"%tel,"的同学录取成功")


if __name__ == "__main__":
        # test()
        studySystem()
        print("1")

