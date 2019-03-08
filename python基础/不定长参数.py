



def add(a,b,*args):
    print("*"*100)
    print(a)
    print(b)
    print(args)

def add2(a,b,*args,**args2):
    print("*"*100)
    print(a)
    print(b)
    print(args)
    print(args2)

if __name__ == "__main__":
    add(1,2)
    add(1,2,12,3,4,5)
    add2(1,2,12,3,4,5,"kakalt",aa = 2,cc = 4,name = 123)
    # //*args 相当于元祖， ** 相当于字典

    print("*"*100)

    #自动拆包的过程
    A = (1,2,3,4,5,6,7,8)
    B ={"name":"卡卡罗特","age":12}
    add2(12,1,*A,*B)

    print("*"*100)
    add2(12,1,*A,**B)