'''
1,导入模块
2,创建套接字
3,设置地址重用
4,绑定端口
5,设置监听 套接字由主动变为被动
6,接收客户端连接
7,接收客户端发送的信息
8,解码数据并进行输出
9,关闭和当前客户端连接
'''
# 1,导入模块
import socket
import threading

def recv_msg(new_client_socket,ip_port):
    while True:
        # 7,接收客户端发送的信息
        recv_date = new_client_socket.recv(1024)
        if recv_date:
            # 8,解码据并进行输出
            recv_text = recv_date.decode()
            print(f"收到{ip_port}的信息：{recv_text}")
        else:
            break
    # 9,关闭和当前客户端连接
    new_client_socket.close()

# 2,创建套接字
tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# 3,设置地址重用
tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
# 4,绑定端口
tcp_server_socket.bind(("",8080))
# 5,设置监听 套接字由主动变为被动
tcp_server_socket.listen(128)
#循环接收客户端连接接收信息
while True:
    # 6,接收客户端连接
    new_client_socket,ip_port = tcp_server_socket.accept()
    print(f"新用户上线，欢迎{ip_port}")
    # recv_msg(new_client_socket,ip_port)
    #创建线程
    threading_recvmeg = threading.Thread(target=recv_msg,args=(new_client_socket,ip_port))
    #设置线程守护
    threading_recvmeg.setDaemon(True)
    threading_recvmeg.start()
# #关闭客户端
# tcp_server_socket.close()

