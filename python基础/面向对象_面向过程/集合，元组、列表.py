



if __name__ == "__main__":
    pass

    a =(1,2,3,4,5,6,7,7898,10)
    b =[1,2,3,4,5,6,7,7898,10]
    c = {1,2,3,4,5,6,7,7898,10}

    print(type(a))
    print(type(b))
    print(type(c))
    type(b)
    print("+++++++++++++++++++++对列表的去重++++++++++++++++++++++++")

    aa =[12,23,12,345,23,12,3,5,6,8,4,6,20,2,4,6,9,0,12]

    # 常规的写法
    aaa = set(aa)
    print(aaa)
    aa = list(aaa)
    print(aa)
    aaaa = tuple(aa)
    print(aaaa)
    # print(aaaa.add(1212))
    print(help(aaaa))
    aaaa = {"12","12"}
    aaaa.add("21")
    aaaa.add("1212")
    aaaa.remove()
    print(aaaa)