
# 存储相同类型的时候用列表
# 否则可以用字典

if __name__ == "__main__":
    list = []
    list.append("1")
    list.append("2")
    list.insert(1,1)
    list.append(12.5)
    list.append("")

    print(list)

    # 增删改查
    list2 = [1,2,3,4,5,6,7,8,9,10]

    list.extend(list2)
    list.remove(1)
    print(list)
    result = list.pop()
    print(result)
    print(list)
    result = list.pop(1)
    print(result)
    print(list)
    list[0] = "卡卡罗特";
    print(list)

    # //查询
    #  in       not in
    if 1 in list:
        print("1111")

    for element in "Python":
        if element == "y":
            pass
        else:
            print(element)