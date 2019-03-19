def test():
    pass

    array = [ ]
    num = 1;
    while num < 100 :
        array.append(num)
        print("%d   "%num,end="")
        num+=1
        if num%5 == 0:
            print()

    print(array)


def test2():
    pass

    array = []
    num = 1;
    for i in range(0,100):
        print("%d   "%i,end="")
        if i%5 == 0:
            print()
        array.append(i)
    print()
    print(array)


def test3():
    pass
    a = [i for i in range(1,100)]
    print(a)

if __name__ == "__main__":
    pass
    test()
    # test2()
    # test3()