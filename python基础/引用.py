


# 和C语言有却别
# 当1个便来你给零i个变量赋值的时候，并不是，把变量复制了一份，二十这个变量的地址也给你可，只想同一个


if __name__ == "__main__":
    print()

    a = 1
    b =a

    # 输出地址
    print(id(a))
    print(id(b))

    # 指向同一个地址

    print("*"*30)
    a = 5
    # 输出地址
    print(id(a))
    print(id(b))
    #python自动检测垃圾