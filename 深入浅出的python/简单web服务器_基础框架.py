#导入模块
import socket
import threading
from application import app
import sys

class WebServer(object):
    #初始化方法
    def __init__(self,port):
        # 创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置地址重用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口
        tcp_server_socket.bind(("", port))
        # 设置监听，让套接字由主动变为被动
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket

    def start(self):
        '''启动web服务器'''
        # 接收客户端连接 设置调用函数
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            # self.request_handler(new_client_socket, ip_port)
            #创建线程对象
            t1 = threading.Thread(target=self.request_handler,args=(new_client_socket,ip_port))
            t1.setDaemon(True)
            t1.start()
        # 关闭操作
        # tcp_server_socket.close()

    def request_handler(self,new_client_socket,ip_port):
        # 接收客户端浏览器发送的请求协议
        recv_date = new_client_socket.recv(1024)
        # 判断协议是否为空
        if not recv_date :
            print(f"{ip_port}客户端已下线")
            new_client_socket.close()
            return
        #使用application 文件中的app模块的application()函数处理
        response_date = app.application("../深入浅出的python2/static", recv_date)
        # 发送响应报文
        new_client_socket.send(response_date)
        new_client_socket.close()

def main():
    '''
    导入模块
    获取系统传递到程序的参数
    判断参数格式是否合格
    判断端口号是否为一个数字
    获取端口号
    在启动web服务器时使用指定端口号
    '''
    # 导入模块
    # 获取系统传递到程序的参数
    params_list = sys.argv
    # 判断参数格式是否合格
    if len(params_list) != 2:
        print("启动失败")
        return
    # 判断端口号是否为一个数字
    if not params_list[1].isdigit():
        print("启动失败，端口号不是纯数字")
        return
    # 获取端口号
    port = int(params_list[1])
    # 在启动web服务器时使用指定端口号
    #创建webserver类的对象
    ws = WebServer(port)
    #对象.start()启动web服务器
    ws.start()


if __name__ == "__main__":

   main()
