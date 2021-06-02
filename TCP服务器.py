###需要在命令行输入ipconfig指令获取本机ip地址
#服务器用于：1.连接多个客户端，获取client_socket并保存到socekts列表  2.接受客户端的信息并转发给所有客户端

from socket import *
from threading import Thread

sockets=[]
def read_send_Msg(client_socket):
    while True:
        recv_data=client_socket.recv(1024)
        if recv_data=='bye':
            ##删除列表中保存的客户端信息并关闭该客户端
            sockets.remove(client_socket)
            client_socket.close()
            break
        if len(recv_data)>0:
            for socket in sockets:
                socket.send(recv_data)
def main():
    server_socket = socket(AF_INET, SOCK_STREAM)
    server_socket.bind(('172.20.10.2',8989))
    server_socket.listen()
    print("服务器上线")
    while True:
        client_socket, client_info = server_socket.accept()
        sockets.append(client_socket)
        t = Thread(target=read_send_Msg, args=(client_socket,))
        t.start()
        wel="连接成功，欢迎登陆！"
        client_socket.send(wel.encode('utf-8'))
if __name__=='__main__':
    main()







