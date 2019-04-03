# conding=utf-8
import socket

sendCount = 0


def createSocketClient():
    while True:
        # 创建 socket 对象
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        # 获取本地主机名
        host = socket.gethostname()

        # 设置端口号
        port = 9999

        # 连接服务，指定主机和端口
        s.connect((host, port))
        # 接收小于 1024 字节的数据
        msg = s.recv(1024)
        # if msg == 0:
        global  sendCount
        sendCount = sendCount + 1
        sendData = "发送数据: " + str(sendCount)
        s.send(sendData.encode('utf-8'))
        # break
        s.close()
        print(msg.decode('utf-8'))


if __name__ == "__main__":
    createSocketClient()
