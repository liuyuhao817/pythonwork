#导入模块
import gevent
from gevent import monkey
monkey.patch_all()
import socket
import threading
class WebServer(object):
    #初始化方法
    def __init__(self):
        # 创建套接字
        tcp_server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 设置地址重用
        tcp_server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, True)
        # 绑定端口
        tcp_server_socket.bind(("", 8080))
        # 设置监听，让套接字由主动变为被动
        tcp_server_socket.listen(128)
        self.tcp_server_socket = tcp_server_socket
        # 定义类的实例属性，porject_dict 初始化为空
        self.porject_dict = dict()  # 创建空字典
        # 定义实例属性 保存要发布的项目路径
        self.currcut_dir = ""
        # 为空字典里面增加键值对    键key               值value
        self.porject_dict['植物大战僵尸-普通版'] = "zwdzjs-v1"
        self.porject_dict['植物大战僵尸-外挂版'] = "zwdzjs-v2"
        self.porject_dict['保卫萝卜'] = "tafang"
        self.porject_dict['2048'] = "2048"
        self.porject_dict['读心术'] = "dxs"

        # 调用初始化游戏项目的方法
        self.init_porject()

        # 给类的初始化方法中配置当前的项目
    def init_porject(self):
     # 2.1.显示所有可能发布的游戏 #返回值是字典里面的所有key 3.0版本里面返回值不在是列表 可以通过list()强制转换
        keys_list = list(self.porject_dict.keys())
            # 遍历所有的key
            # enumerate(keys_list)会将我们的列表里面的数据添加一个索引序列
            # 例如 原本打印keys_list ['植物大战僵尸-普通版'，'植物大战僵尸-外挂版'，，，，，，]
            # 加了eunmerate后 就是[(0,'植物大战僵尸-普通版'),(1,'植物大战僵尸-外挂版'),........]
        for index, game_name in enumerate(keys_list):
            print("%d.%s" % (index, game_name))
            # 2.2.接收用户的选择
        sel_no = int(input('请选择要发布的游戏序号：'))
            # 2.3.根据用户选择发布指定项目(保存用户选择的游戏的指定目录)
        key = keys_list[sel_no]
            # 根据字典key得到项目具体路径
        self.currcut_dir = self.porject_dict[key]
        # 3.更改web服务器打开的文件目录

    def start(self):
        '''启动web服务器'''
        # 接收客户端连接 设置调用函数
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            # # 创建线程对象
            # t1 = threading.Thread(target=self.request_handler, args=(new_client_socket, ip_port))
            # #线程守护
            # t1.setDaemon(True)
            # t1.start()
            gevent.spawn(self.request_handler, new_client_socket, ip_port)
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
        # 根据客户端浏览器请求的资源路径，返回请求协议
        # 1)把请求协议解码，得到请求报文的字符串
        request_text = recv_date.decode()
        # 2)得到请求行
        #     查找第一个\r\n出现的位置
        loc = request_text.find("\r\n")
        #      截取字符串 从头开始截取 第一个\r\n出现的位置
        request_line = request_text[:loc]
        # 把请求行按照空格拆分 得到列表  split 按照指定字符分割字符串 返回一个列表 丢失分割字符
        request_line_liat = request_line.split(" ")
        # 得到请求资源路径
        file_path = request_line_liat[1]
        # 设置默认首页 当客户端未指定请求内容时 默认返回index。html
        if file_path == "/":
            file_path = "/index.html"
        # 拼接响应的报文
        # 响应行
        response_line = "HTTP/1.1 200 OK\r\n"
        # 响应头
        response_header = "Server : Python20ws/2.1\r\n"
        response_header += "Content-Type: text/html\r\n"
        # 响应空行
        response_blank = "\r\n"
        # 响应主体
        # response_body =  "Hello World"
        #************返回固定页面***************
        #通过with open 读取文件
        #设置异常捕获 当客户端访问页面不存在 出现异常时
        try:
            with open(self.currcut_dir+file_path,"rb") as file :
                response_body = file.read()
        except  Exception as e :
            #重新修改响应行为404
            response_line = "HTTP/1.1 404 Not Found\r\n"
            #响应内容为错误
            response_body = "Error! (%s)" % str(e)
            #把响应内容转换为字节码
            response_body = response_body.encode()
        # 拼接响应报文
        response_date = (response_line + response_header +response_blank).encode() +response_body
        # 发送响应报文
        new_client_socket.send(response_date)
        new_client_socket.close()

def main():

    #创建webserver类的对象
    ws = WebServer()
    #对象.start()启动web服务器
    ws.start()


if __name__ == "__main__":

   main()
