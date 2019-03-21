# coding=utf-8
import random
import time


class GunLaowang(object):
    def __init__(self, name):
        # super(GunLaowang,self).__init__()
        super(GunLaowang).__init__()
        self.name = name
        self.gun = None #  保存抢多向的引用
        self.hp = 100

    def papapa(self):
        print("===============%s" % self.name)

    # 装弹夹
    def installDanJia(self, danjia_temp, zidan_temp):
        danjia_temp.saveZd(zidan_temp)

    # 装抢
    def zhuangDanjiaToGun(self,gun, danjia):
        gun.zhuangDanjiaToGun(danjia)

    # 拿起枪
    def takeGun(self,gun):
        self.gun = gun

    def __str__(self):
        if self.gun :# 有抢支弹药
            return "%s 有枪，其战斗力为%d"%(self.name,self.hp)
        else:
            self.hp = 0
            return "%s 没有枪，其战斗力为%d"%(self.name,self.hp)

    def shoutEnemy(self,gun, enemy):
        gun.shoutFire(enemy)


class Gun(object):
    pass

    def __init__(self, name):
        super(Gun).__init__()
        self.name = name
        self.danjia = None  # 用于保存弹夹

    def zhuangDanjiaToGun(self, danjia):
        self.danjia = danjia

    def shoutFire(self, enemy):
        print("该枪%s 向%s发射了子弹"%(self.name,enemy.name))
        # 先从弹夹中你那个取出子弹，
        zidan = self.danjia.takeOutZidan()
        if zidan:
            zidan.shoutToEnemy(enemy)
        else:
            print("开枪射击失败，没子弹啦")
            pass

    def __str__(self):
        # 如果有弹夹，则显示弹夹
        if self.danjia:
            return "抢的名称为：%s ,拥有的弹夹为%s"%(self.name,self.danjia.__str__())
        else:
            return "抢的名称为：%s ,该强中没安装弹夹~~"%(self.name)
class Danjia(object):
    def __init__(self, max_num):
        super(Danjia).__init__()
        self.max_num = max_num  # 子弹的最大数目
        self.zidanList = []  # 用来存放所有子弹的引用

    def saveZd(self, zidan_temp):
        self.zidanList.append(zidan_temp)

    def takeOutZidan(self):
        """弹出最上面的那个子弹"""
        if self.zidanList:
            return self.zidanList.pop()
        else:
            return None

    def __str__(self):
        message = "弹夹的信息（%d, 持有%d子弹）"%(len(self.zidanList),self.max_num)
        print(message)
        return message


class ZiDan(object):
    pass

    def __init__(self, shoutNum):
        super(ZiDan).__init__()
        self.enemy = None

    def shoutToEnemy(self,enemy):
         self.enemy = enemy
         enemy.sunDoution()

# 创建一个敌人
class Enemy(object):
    pass

    def __init__(self, name):
        super(Enemy).__init__()
        self.name = name
        self.hp = random.uniform(5,106)

    def __str__(self):
        message = "哈哈，我是敌人：%s ，拥有血量：%d 滴"%(self.name,self.hp)
        print(message)
        return message

    def sunDoution(self):
        if int(self.hp) <= 0:
            print(" 没血啦，I am dead")
        elif int(self.hp) == 1:
            self.hp -=1
            print("I am a enemy ，姓名叫：%s ,%d 滴血用完，游戏结束"%(self.name,self.hp))
        else:
            self.hp -=1
            print("I am a enemy ，姓名叫：%s ,还剩下 %d 滴血"%(self.name,self.hp))


def sleep_time(hour, min, sec):
    return hour * 3600 + min * 60 + sec
# 时间间隔
second = sleep_time(0, 0, 2)

if __name__ == "__main__":
    pass
    # 创建一个老王对象
    laowang = GunLaowang("老王")
    laowang.papapa()

    # 创建一个枪
    gun = Gun("AK47")

    # 创建一个弹夹
    danjia = Danjia(100)


    # 创建一些子弹
    #zidan = ZiDan(10)
    for i in range(20):
        zidan = ZiDan(10)
        laowang.installDanJia(danjia,zidan)

    # 老王把子弹装到弹夹里面去
    laowang.installDanJia(danjia,zidan)

    # 老王把弹夹撞到抢里面去
    laowang.zhuangDanjiaToGun(gun,danjia)

    # 老王拿起枪
    laowang.takeGun(gun)

    # 创建一个敌人
    enemy = Enemy("老宋")
    enemy.__str__()

    # 老王开始射击啦
    shoutNum = round(random.uniform(6,102))
    print("**************************************************")
    print("准备要想老王发射%d"%(shoutNum))
    print("...")
    print()
    # for i in range(shoutNum):
    #     laowang.shoutEnemy(gun,enemy)
    print("每个%d秒进行发射~~~"%(second))
    while True:
        print("还剩下%d滴血~~~"%(enemy.hp))
        if int(enemy.hp)<= 0:
            print("===== .....Game over.....=======")
            break
        elif not danjia.zidanList:
            break
        else:
            time.sleep(0.5)
            laowang.shoutEnemy(gun,enemy)
    # print(gun.__str__())
    # danjia.__str__()
    # print(laowang.__str__())


