from socket import *
from threading import Thread

def readMsg(client_socket):
    while True:
        recv_data=client_socket.recv(1024)
        print(recv_data.decode('utf-8'))
def writeMsg(client_socket,user_name):
    while True:
        msg=input('>')
        Msg=user_name+':' +msg
        client_socket.send(Msg.encode('utf-8'))

client_socket=socket(AF_INET,SOCK_STREAM)
client_socket.connect(('172.20.10.2',8989))
user_name=input('请输入用户名：')
read_thread=Thread(target=readMsg,args=(client_socket,))
write_thread=Thread(target=writeMsg,args=(client_socket,user_name))

read_thread.start()
write_thread.start()

read_thread.join()
write_thread.join()

client_socket.close()