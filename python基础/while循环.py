import random

#打印水仙花
def printFlower():
    num =1
    while num <10:
        print("*" *num)
        num = num+1


# 利用python打印一个乘法口诀
def printWhileNumTab():
    i = 0

    while i < 9:
        i = i+1
        j = 0
        while j < i:
            j+=1
            print("%d * %d = %d\t"%(j,i ,i *j),end="")
        j = 0
        print("")





# 利用python打印一个乘法口诀
def printForNumTab():
    print("")
    for i in range(1,10):
        for j in range(1,10):
            print("%d * %d = %d\t"%(j,i ,i *j),end="")
            if i < j+1:
                break
        print("")










def printNumTab2():

    aa = [0,1,2,3,4,5,6,7,8,9,10]
    for i in aa :
        a = random.randint(0,10)
        print("%d\t"%a,end="")
        a +=1


def forxu():
    print("\n***************************************forxu**********************************************")
    name = "阿发案发地阿斯顿发地方艾弗森撒打算"
    for i in name:
        print("%s\t"%i,end="")


if __name__ == "__main__":
    print("")

    a =5
    num = 1;
    while num < 15:
        print("this is the %d"%a)
        num = num+1
        if num <5:
            num = num+3
            break

    print("while 循环的学习" * 10 +"\n")

    printFlower()
    printWhileNumTab()
    printNumTab2()
    forxu()
    printForNumTab()