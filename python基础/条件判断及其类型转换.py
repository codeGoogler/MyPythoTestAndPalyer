def test():

    types = 0;
    a = input("请输入您的年龄：")
    if int(a) >60:
        print("请休息吧，不符合工作")
    elif int(a) >80:
        print("看来还有点余地~~~")
    else:
        print("年入百岁，赶紧退休吧~~")
if __name__ == "__main__":
    test()
