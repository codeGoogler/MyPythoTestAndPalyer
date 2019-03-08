
def printLn(a ,b):
    if not a.isdigit():
        print("您输入的不是数字")
        return -1
    elif (not b.isdigit()):
        print("您输入的不是数字")
        return -1
    c = int(a) * int(b);
    print("%d x %d = %d"%(int(a), int(b), c))
    return aa(c)


def aa(c):
    if c > 1000:
        return 4
    elif 50 < c <= 80:
        return 1
    elif 80 > c > 30:
        return 2
    elif 30 >= c > 0:
        return 3
    elif c == 0:
        return 5

if __name__ == "__main__":
    while True:
        a = input("请输入一个数字：")
        b = input("请再输入一个数字：")
        i = printLn(a, b)
        if i == 1:
            print("成绩及格 ，成绩非常优异 荣获等级A")
        elif i == 2:
            print("成绩及格, 荣获等级B")
        elif i == 3:
            print("成绩不及格, 荣获等级C")
        elif i == 4:
            print("成绩无效, ELD")
        elif i == 5:
            print("未参加考试, 荣获等级D")


def a(x, y):
    if x == y:
        return x, y
