




if __name__ == "__main__":
    a = "yuerLoveCoding"

    a1 = a[0:]
    print(a1)

    a2 = a[:len(a)]
    print(a2)

    a3 = a[3:10]
    print(a3)

    print("a %s"%a)
    print("a[-0] %s"%a[-len(a)])

    a32 = a[3:-1]
    print(a32)


    # [起始位置，终止位置，步长(隔着取，默认为 1)]
    a4 = a[1:-1:1]
    print(a4)

    a4 = a[1:-1:2]
    print(a4)



    # //逆序即时倒叙
    a5  = a[-1::-1]
    print(a5)