# conding=utf-8
import socket


def createSocketService():
    # 导入 socket、sys 模块
    import socket
    import sys

    # 创建 socket 对象
    serversocket = socket.socket(
        socket.AF_INET, socket.SOCK_STREAM)

    # 获取本地主机名
    host = socket.gethostname()

    port = 9999

    # 绑定端口号
    serversocket.bind((host, port))
    # serversocket.bind("10.2.0.215", port)

    # 设置最大连接数，超过后排队
    serversocket.listen(5)

    # 建立客户端连接

    while True:
        clientsocket, addr = serversocket.accept()
        print("连接地址: %s" % str(addr))

        type = input("请输入要发送的值：")
        if isinstance(type, int):
            if type == 0:
                break
            else:
                continue
        elif len(type) > 0:
            msg = type
            clientsocket.send(msg.encode('utf-8'))
        # msg='欢迎访问菜鸟教程！'+ "\r\n"

        print("接收到的数据：%s"%(clientsocket.recv(1024).decode("utf-8")))
        clientsocket.close()

if __name__ == "__main__":
    createSocketService()
