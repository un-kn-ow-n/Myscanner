import socket
import os

server_ip = "172.20.34.67"
client_ip = "172.20.161.116"
server_port = "1280"
client_port = "1290"

class Packet():
    def __init__(self, sip, tip, sp, tp, op, content):
        self.sip = sip
        self.tip = tip
        self.sp = sp
        self.tp = tp
        self.op = op
        self.content = content

    def parseStr(trans):
        lines = trans.split(b"\n", 2)
        temp = lines[0].decode()
        address = temp.split(" ")
        sip = address[0]
        tip = address[1]
        sp = address[2]
        tp = address[3]
        op = lines[1].decode().split(" ")[0]
        content = lines[2]
        return Packet(sip, tip, sp, tp, op, content)

    def toTrans(self):
        firstline = (self.sip + " " + self.tip + " " +
                     self.sp + " " + self.tp + "\n" + self.op).ljust(79, " ") + "\n";
        return firstline.encode("utf-8") + self.content

def getlist():
    return os.listdir("tosend")


def showlist(list):
    for fname in list:
        print(fname)


def send(tosend):
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", int(client_port)))
    except socket.error as msg:
        print("套接字创建失败。\n========================================")
        return

    try:
        s.connect((server_ip, int(server_port)))
    except:
        print("服务器连接失败。\n========================================")
        s.close()
        return
    print("成功连接 " + server_ip + " 的 " + str(server_port) + " 端口。")

    with open("tosend/" + tosend, "rb") as file_object:
        print("开始发送 " + tosend + " 。")

        try:
            s.send(Packet(client_ip, server_ip, client_port, server_port, "SEND", b"").toTrans())
            while True:
                temp = file_object.read(1024 - 80)
                if temp == b"":
                    break
                packet = Packet(client_ip, server_ip, client_port, server_port, "DATA", temp)
                s.send(packet.toTrans())

        except:
            print("发送文件失败。\n========================================")
            s.close()
            return
        finally:
            file_object.close()
    print("发送文件成功。\n========================================")
    s.close()
    return

def download():
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind(("", int(client_port)))
    except socket.error as msg:
        print("套接字创建失败。\n========================================")
        return

    try:
        s.connect((server_ip, int(server_port)))
    except:
        print("服务器连接失败。\n========================================")
        s.close()
        return
    print("成功连接 " + server_ip + " 的 " + str(server_port) + " 端口。")
    s.send(Packet(client_ip, server_ip, client_port, server_port, "DOWNLOAD", b"").toTrans())
    data = s.recv(1024)
    try:
        packet = Packet.parseStr(data)
        files = packet.content.decode()
    except:
        print("报文格式不正确。")
        return
    lines = files.split(" ")
    for file in lines:
        if file != "":
            print(file)
    while True:
        print("请输入要下载的文件名(back返回上一步):\n========================================")
        todownload = input()
        if todownload != "" and todownload in lines:
            s.send(Packet(client_ip, server_ip, client_port, server_port, "DOWNLOAD", todownload.encode()).toTrans())
            print("开始下载 " + todownload + " 。")
            with open("file_download/" + todownload, "wb") as file:
                flag = False
                while True:
                    data = s.recv(1024)
                    if data == b"":
                        break
                    while len(data) != 1024:
                        temp = s.recv(1024 - len(data))
                        if temp == b"":
                            flag = True
                            break
                        data += temp
                    try:
                        packet = Packet.parseStr(data)
                    except:
                        print("报文格式不正确。")
                        return
                    file.write(packet.content)
                    if flag:
                        break
            print("下载文件成功。\n========================================")
            return
        elif todownload == "back":
            return
        else:
            print("不存在该文件。")


if __name__ == "__main__":
    print("欢迎使用文件发送/下载客户端!")
    while True:
        print("请输入操作指令：\nsend:发送文件\n" +
              "download:下载文件\nquit:退出\n========================================")
        answer = input();
        if answer == "send":
            flist = getlist()
            showlist(flist)
            while True:
                print("请输入要发送的文件名(back返回上一步):\n========================================")
                tosend = input()
                if tosend in flist:
                    send(tosend)
                    break
                elif tosend == "back":
                    break
                else:
                    print("不存在该文件。")
        elif answer == "download":
           download()
        elif answer == "quit":
            print("谢谢使用。")
            break
        else:
            print("无此操作指令，请重新输入。")
