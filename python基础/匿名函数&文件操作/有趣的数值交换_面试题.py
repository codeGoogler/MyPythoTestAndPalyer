def test01():
    a = 4
    b = 5

    c = 0
    c = a
    a = b
    b = c
    print("a = %d , b =%d " % (a, b))


def test02():
    pass
    a = 4
    b = 5

    a = a + b
    b = a - b
    a = a - b
    print("a = %d , b =%d" % (a, b))


def test03():
    pass
    a = 4
    b = 5
    a, b = b, a
    print("a = %d , b =%d" % (a, b))


if __name__ == "__main__":
    test01()
    test02()
    test03()
