def foo():
    str = "function"
    print(str)


def foo1(num):
    print('num', num)


def foo2(name, age):
    print('name', name)
    print('age', age)



# def是一个注册
def sss():
    print("asdfasdfasdf")
    a = 100
    if a >= 0:
        print(a)
        print("完全结束了！！！！")
    else:
        print(-a)

    sum = 0;
    for i in [0,1,2,3,4,5,6,7]:
        sum = sum +i
        print(sum)

if __name__ == "__main__":
    # print("main")
    # foo2('yuhui', 30)
    # foo1(6)
    sss()
