
# if __name__ == "__main__":
#     print("==================")


def foo2(name, age):
    print('name', name)
    print('age', age)

def foo3(name, age):
    print('name', name)
    print('age', age)


def test():

    # 可以代表单行注释
    print("`1231`123`13123`13123")
    """
    print("`1231`123`13123`13123")
    print("`1231`123`13123`13123")
    print("`1231`123`13123`13123")
    print("`1231`123`13123`13123")
    """
    print("`1231`123`13123`13123")

    '''
    print("`1231`123`13123`13123")
    print("`1231`123`13123`13123")
    print("`1231`123`13123`13123")
    print("`1231`123`13123`13123")
    '''

    a = 100
    b = 100
    c= 100
    e = a +b + c
    print(e)
    print(e*e)


if __name__ == "__main__":
    test()
