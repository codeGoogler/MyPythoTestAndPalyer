# 在python中，所有的操作都是引用传递，而不是值传递



# 值传递还是引用传递
#
# Python参数传递统一使用的是引用传递方式。因为Python对象分为可变对象(list,dict,set等)和不可变对象(number,string,tuple等)，当传递的参数是可变对象的引用时，因为可变对象的值可以修改，因此可以通过修改参数值而修改原对象，这类似于C语言中的引用传递；当传递的参数是不可变对象的引用时，虽然传递的是引用，参数变量和原变量都指向同一内存地址，但是不可变对象无法修改，所以参数的重新赋值不会影响原对象，这类似于C语言中的值传递。
# 所以回到上面的问题引出，变量“a”，“b”，“val1”，“val2”其实都指向同一可变对象的内存地址，当通过变量“val2”对对象进行修改时，其他变量的值也相应被修改了。
# ---------------------
# 作者：zxhohai
# 来源：CSDN
# 原文：https://blog.csdn.net/hohaizx/article/details/78427406
# 版权声明：本文为博主原创文章，转载请附上博文链接！

a = 100
aa = [1]


def test(a):
    a = a + 100
    print("test：%d"%a)
    return a

def test1(a):
    a = a + a
    print("test：%d"%a)
    return a

def test2(a):
    a = a + a
    print(a)
    return a

if __name__ == "__main__":
    # test(a)
    # print("main方法里面的：%d"%a)
    # test1(aa[0])
    # print(aa)
    test2(aa)
    print(aa)