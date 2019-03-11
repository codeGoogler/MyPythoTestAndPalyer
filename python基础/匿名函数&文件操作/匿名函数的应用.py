import print as print


def test01():
    pass
    list = [0, 102, 23, 0, 21, 314, 234, 11, 2, 3, 4, 5, 6, 7, 8, 9, 0]
    list.sort()

    print()
    list.sort(reverse=True)
    print(list)
    print()
    list.sort(reverse=False)
    print(list)


def test02():
    pass
    list = [
        {"name": "张三", "age": 18},
        {"name": "老师", "age": 12},
        {"name": "王五", "age": 0},
        {"name": "赵柳", "age": 123},
        {"name": "于亚豪", "age": 13458},
        {"name": "联系", "age": 186},
        {"name": "阿牛", "age": 186},
    ]
    list.sort(key=lambda x: x['age'])
    print(list, end="")


def test03(a,b,func):
    pass
    result = func(a,b)
    print("最终显示结果：%d"%result)
    return result

if __name__ == "__main__":
    test01()
    print()
    print()
    test02()
    print()
    print()

    test03(5,2,lambda x,y: x * y)
