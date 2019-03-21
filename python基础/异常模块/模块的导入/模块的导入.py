import sys
import test01

if __name__ == "__main__":
    print(sys.path)
    test01.papaAbao()

# 1、 搜索路径的时候，sys.path
# 2、重新导入
#   from imp import  *
#   import xxxx
    reload(test01)
#
#
#
#
#