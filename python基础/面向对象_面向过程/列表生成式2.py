


def test1():
    e = [i for i in range(1,10) for j in range(2) ]
    print(e)


def test2():
    pass
    e = [i for  i in  range(20) if i%5==0]
    print(e)

def test3():
    pass
    e = [(i,j) for  i in  range(20) for j in range(3)]
    # e = ((i,j) for  i in  range(20) for j in range(3))
    print(e)




if __name__ == "__main__":
    pass
    print("=================")
    test1()
    test2()
    test3()