import copy


# api说明
# == 是判断这个值是否相等
# is 是判断是不是指向同一个内存地址



if __name__ == "__main__":
    pass

    a = 100
    b = 100

    print(a == b)
    print(a is b)

    aa = 1000
    bb = copy.deepcopy(aa)

    print(aa == bb)
    print(aa is bb)

    aaa = [1,2,3,4,5]
    bbb = [1,2,3,4,5]
    ccc = copy.copy(aaa)
    print(aaa == bbb)
    print(aaa is bbb)

    print(aaa == ccc)
    print(aaa is ccc)