
 # 第一种方式调用模块，import 模块的名字
import  异常
def test01():
    pass
    异常.test03()



 # 第二种方式调用模块，from 模块的名字 import
from 异常处理 import yiachangPapapa

def test02():
    pass
    yiachangPapapa()





# 第三种方式调用模块 导入所有  ，from 模块的名字 import *
from 异常处理 import *

def test03():
    pass
    yiachangPapapa()
    yiachangPapapa2()





if __name__ == "__main__":
    # sssTest()
    a = "aaa aaa"
    b = "aaa aaa"
    print(a is b)
    test01()
    test02()
    test03()