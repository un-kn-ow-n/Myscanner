import socket
import threading

lock = threading.Lock()
output = ""

def iptoint(ip_str):
    temp = ip_str.split(".")
    return int(temp[0]) * (256 ** 3) + int(temp[1]) * (256 ** 2) + int(temp[2]) * 256 + int(temp[3])

def iptostr(ip_int):
    return str(ip_int // (256 ** 3)) + "." + str((ip_int % (256 ** 3)) // (256 ** 2)) + "." + str((ip_int % (256 ** 2)) // 256) + "." + str(ip_int % 256)

def scan(addresslist):
    for address in addresslist:
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.settimeout(0.5)
        result = s.connect_ex(address)
        if result == 0:
            lock.acquire()
            print(address[0] + ":" + str(address[1]) + " is open.")
            global output
            output += address[0] + ":" + str(address[1]) + " is open.\n"
            lock.release()
        s.close()

def assign(start_ip, end_ip, start_port, end_port, thread_num):
    threadlist = []
    addresslists = []
    for i in range(thread_num):
        addresslists.append([])
    for ip in range(iptoint(start_ip), iptoint(end_ip) + 1):
        for port in range(start_port, end_port + 1):
            addresslists[(ip + port) % thread_num].append((iptostr(ip), port))
    for i in range(0, thread_num):
        t=threading.Thread(target=scan, kwargs={'addresslist': addresslists[i]})
        t.start()
        threadlist.append(t)
    return threadlist


def assign_and_scan(start_ip, end_ip, start_port, end_port, thread_num):
    for t in assign(start_ip, end_ip, start_port, end_port, thread_num):
        t.join()
    global output
    copy = output
    output = ""
    return copy