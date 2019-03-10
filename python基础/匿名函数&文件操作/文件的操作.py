import os


def test3():
    try:
        print("*" * 20)
        fAA = open("G:\\del_python_study\\AA.txt", "r+")
        fBB = open("G:\\del_python_study\\BB.txt", "r+")
        fCC = open("G:\\del_python_study\\BBC.txt", "w+")
        while True:
            content = fAA.read(10)
            fCC.write(content)
            fCC.flush()
            if fAA.tell() > 100:
                break
        fCC.write(fBB.read())
        fCC.flush()
        print("end" * 20)

        print(fAA.read())
        fAA.close()
        # fBB.close()
        # fCC.close()
    except FileNotFoundError:
        print("File is not found.")
    except EOFError:
        print("You don't have permission to access this file.")


def freadLine():
    f = open("G:\\python_study2.txt", "r+")
    fileName = f.name
    ss = f.readlines()
    print(ss)
    f.seek(0)
    ss = f.readline()
    # print(ss)
    pos = f.tell()
    print("当前位置: %d" % (pos))


def copyFile():
    pass
    f = open("G:\\python_study2.txt", "r+")
    fileName = f.name
    posion = fileName.rfind(".")
    newNameDile = fileName[0:posion] + "[复制]" + fileName[posion:]
    f2 = open(newNameDile, "w+")
    os.system("ls -a > 1.txt")
    f2.write(f.readlines())
    f.close()
    f2.close()


def test():
    print("文件的操作")
    f = open("G:\\python_study2.txt", "r+")
    # f.close()
    print("文件名: %s" % f.name)
    # print("是否已关闭 : %t"%f.closed)
    # print("访问模式 :  %s"%f.mode)
    # print("末尾是否强制加空格 :  %s"%f.softspace)
    f.write("a\n")
    f.write("b\n")
    f.write("c\n")
    f.write("d\n")
    f.write("1\n")
    # f.flush()
    ss = f.read(1)
    print(f.read(1024))
    f.close()

    # print("===============")
    # test()
    # copyFile()
    # freadLine()


def test4():
    pass
    i = 0
    while True:
        print("%d "%i,end="")
        i = i+1
        if i > 1000:
            break

if __name__ == "__main__":
    test3()
    # test4()