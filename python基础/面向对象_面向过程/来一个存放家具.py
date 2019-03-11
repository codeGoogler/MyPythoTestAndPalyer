



class Home:

    def __init__(self,people,new_area,space,num):
         self.people = people
         self.new_area = new_area
         self.space = space
         self.left_arae = space
         self.num = num
         self.coloctAllItem = []

    @property
    def __str__(self):
        if len(self.coloctAllItem) > 0:
            allItem = ""
            for item in self.coloctAllItem:
               # print( allItem = allItem+item)
               # print(item.name)
               if not allItem.endswith(",") and not len(allItem):
                   allItem =allItem+ item.name
               else:
                   allItem = allItem+" ， "+item.name
               # allItem =  allItem.join(item.name).join(",")
               # print("111：%s 111"%allItem)
            mes = "我有一个老家，老家是：%s,我家有%d口人，分别是：%s,我家非常大，占地面积为：%0.2f平方米,其中家里面有好多家具：%s"%(self.space,self.num,self.people,self.new_area,allItem)
        else:
            mes = "我有一个老家，老家是：%s,我家有%d口人，分别是：%s,我家非常大，占地面积为：%0.2f平方米"%(self.space,self.num,self.people,self.new_area)
        return mes

    # 添加一个家具
    def addItemFurniture(self,item):
        print("增加了一个家具：%s"%item.name)
        self.new_area = self.new_area - item.area
        self.coloctAllItem.append(item)

    # 出生了一个小孩子
    def addChild(self,people):
        self.num += 1
        self.people = self.people+","+ people.name
        print(self.people)

class Chirld:

    def __init__(self,name,weight,sex):
        self.name = name
        self.weight = weight
        self.sex = sex

    def __str__(self):
        return "出生了一个小孩：姓名：%s  ,性别：%s ,体重：%.2f千克"%(self.name,self.sex,self.weight)


class Bed:

    def __init__(self,name ,new_area):
        self.area = new_area
        self.name = name

    def __str__(self):
        return "添加了一张床：%s, 占地面积为：%0.2f平方米"%(self.name,self.area)


if __name__ == "__main__":

    home = Home("爸爸，妈妈，爷爷，奶奶 ，我 ",98.6,"河南林村",4)
    print(home.__str__)

    bed = Bed("席慕思床",4.6)
    bed2 = Bed("木床",5.6)
    bed3 = Bed("弹簧床",4)
    print(bed.__str__())

    duoduo = Chirld("baby",12.5,"男")
    print(duoduo.__str__())

    home.addChild(duoduo)
    home.addChild(duoduo)
    home.addChild(duoduo)
    home.addItemFurniture(bed)
    home.addItemFurniture(bed2)
    home.addItemFurniture(bed3)
    print(home.__str__)