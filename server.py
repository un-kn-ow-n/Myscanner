import socket
import os

server_ip = "172.20.54.123"
server_port = "1280"


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
        firstline = (self.sip + " " + self.tip + " " + self.sp + " " + self.tp + "\n" + self.op).ljust(79, " ") + "\n";
        return firstline.encode("utf-8") + self.content

def getlist():
    return os.listdir("todownload")


def filelist(list):
    files = ""
    for fname in list:
        files += fname + " "
    return files.encode()

if __name__ == "__main__":
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind(("", int(server_port)))
    print("这里是文件发送/下载服务器端，监听中……\n========================================");
    counter = 1
    s.listen()
    while True:
        conn, addr = s.accept()
        print("收到连接请求。")
        try:
            request = Packet.parseStr(conn.recv(80))
        except:
            print("报文格式不正确。\n========================================")
            conn.close()
            continue
        print(request.op)
        if request.op == "SEND":
            print("开始接收文件。")
            with open("file_recv/file" + str(counter), "wb") as file:
                flag = False
                while True:
                    data = conn.recv(1024)
                    while len(data) != 1024:
                        temp = conn.recv(1024 - len(data))
                        if temp == b"":
                            flag = True
                            break
                        data += temp
                    try:
                        packet = Packet.parseStr(data)
                    except:
                        print("报文格式不正确。")
                        break
                    file.write(packet.content)
                    if flag:
                        break
            counter += 1
            print("文件接收成功。\n========================================")
            conn.close()
        elif request.op == "DOWNLOAD":
            flist = getlist()
            files = filelist(flist)
            print("发送文件列表。")
            conn.send(Packet(server_ip, request.sip, server_port, request.sp, "SHOW", files).toTrans())
            try:
                todownload = Packet.parseStr(conn.recv(1024)).content.decode()
            except:
                print("报文格式不正确。")
                todownload = ""
            if todownload not in flist:
                print("无此文件。" + todownload)
            else:
                with open("todownload/" + todownload, "rb") as file_object:
                    print("开始发送 " + todownload + " 。")

                    try:
                        while True:
                            temp = file_object.read(1024 - 80)
                            if temp == b"":
                                break
                            packet = Packet(server_ip, request.sip, server_port, request.sp, "DATA", temp)
                            conn.send(packet.toTrans())

                    except:
                        print("发送文件失败。\n========================================")
                        s.close()

                    finally:
                        file_object.close()
                print("发送文件成功。\n========================================")
            conn.close()
        else:
            print("无法识别该操作。\n========================================")

            