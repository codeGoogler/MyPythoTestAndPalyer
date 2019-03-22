#coding=utf-8
import  turtle as t
import copy


if __name__ == "__main__":
    pass
# 浅拷贝： 不同的引用指向同一地址, 仅仅是对这个地址备份了一份 ，浅拷贝相当于共享的,  对于不可变类型，直接的是地址
    a = [1,2,3,4,5]
    b =a
    b.append(6)
    print(id(a))
    print(id(b))

    print(a)
    print(b)
# 浅拷贝：直接把内存里面的内容玩玩全完的复制了一份，另外开辟了一个内存空间，
#  copy。copy ，对于不可变内容，直接相当于浅拷贝，对于可变内容 ，只对该对象的第一层进行copy
    c = copy.copy(a)
    c.append(100)
    print(id(c))
    d = copy.deepcopy(a)
    d.append(7)
    print(id(d))
    d.append(1000)
    print(c)
    print(d)

    aa = [1,2,3,4]
    bb = [1,2,3,4]
    cc = [aa,bb]

    dd = copy.copy(cc)
    ee = copy.deepcopy(cc)

    print("")
    print("============================")
    print(dd[0])
    print(ee[0])
    print(cc[0])

    print(id(cc))
    print(id(dd))
    print(id(ee))
