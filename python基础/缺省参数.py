# 什么是缺省参数？
#    在方法的形参中，给一个参数设定一个默认值，调用该方法是，可以不传入这个设置默认值的参数。调用的时，如果你调用🔟，给了这个参数一个新的值，那么执行结果就会用心的值来代替设置默认的值，否则，直接用该默认是进行方法调用
# 也可以直接指定形参里面的参数 c =2, 可以变量名= ，但是这些变量名要去形参里面的参数（命名参数）

def add(a=1, b=2, c=1):
    result = a + b + c
    return result


if __name__ == "__main__":
    print(add(1, 2, 3))
    print(add(1, 2, 1))
    print(add(1, 1))
    print(add(1))
    print(add())
    print(add(c=2))

    # 一个常见的案例
    # print(value, ..., sep=' ', end='\n', file=sys.stdout, flush=False)
    print()#后面都是缺省参数
    help(print)
