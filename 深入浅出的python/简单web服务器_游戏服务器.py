#导入模块
import socket
from application import app
import sys

'''
1.给类的初始化方法中配置当前的项目
{'2048':'/.2048',"植物大战僵尸":'zwdzjs-v1',......}
2.给类增加一个初始化项目配置的方法 init_porjectd()
2.1。显示所有可能发布的游戏
2.2.接收用户的选择
2.3.根据用户选择发布指定项目(保存用户选择的游戏的指定目录)
3.更改web服务器打开的文件目录
'''

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
        # 定义类的实例属性，porject_dict 初始化为空
        self.porject_dict = dict()#创建空字典
        #定义实例属性 保存要发布的项目路径
        self.currcut_dir = ""
        #为空字典里面增加键值对    键key               值value
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
        #遍历所有的key
    # enumerate(keys_list)会将我们的列表里面的数据添加一个索引序列
    # 例如 原本打印keys_list ['植物大战僵尸-普通版'，'植物大战僵尸-外挂版'，，，，，，]
    # 加了eunmerate后 就是[(0,'植物大战僵尸-普通版'),(1,'植物大战僵尸-外挂版'),........]
        for index, game_name in enumerate(keys_list):
            print("%d.%s" %(index,game_name))
    # 2.2.接收用户的选择
        sel_no = int(input('请选择要发布的游戏序号：'))
    # 2.3.根据用户选择发布指定项目(保存用户选择的游戏的指定目录)
        key = keys_list[sel_no]
        #根据字典key得到项目具体路径
        self.currcut_dir = self.porject_dict[key]
    # 3.更改web服务器打开的文件目录


    def start(self):
        '''启动web服务器'''
        # 接收客户端连接 设置调用函数
        while True:
            new_client_socket, ip_port = self.tcp_server_socket.accept()
            self.request_handler(new_client_socket, ip_port)
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
        response_date = app.application(self.currcut_dir, recv_date)
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
