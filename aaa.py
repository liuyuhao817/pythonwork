# prompt = "hello world"
# prompt +='\nhello python '
#
# name = int(input(prompt))
# print(f'{name}')


# message=int(input("请问有多少人就餐："))
# if message > 8 :
#     print("不好意思，没有座位了")
# else:
#     print('欢迎光临')

# message = int(input("请输入数值："))
# if message % 10==0:
#     print('是倍数')
# #
# # else:
# #     print('不是倍数')
#
# message = ''
# prompt = "hello world"
# prompt +='\nhello python '
# while message != 'quit':
#     message=input(prompt)
#     if message != "quit":
#         print(message)


# active = True
# while active:
#     message = input('hello world: ')
#     if  message =='quit':
#         active = False
#     else:
#         print(message)

# unconfirmed_users = ['alice','brian','candace']
# confirmed_users = []
#
# while unconfirmed_users:
#     current_user = unconfirmed_users.pop()
#
#     print(f'Verifying user: {current_user.title()}')
#     confirmed_users.append(current_user)
#
# print('\nThe following users have been confirmed: ')
# for confirmed_user in confirmed_users:
#     print(confirmed_user.title())

# pets = ['cat','csa','cat','vcss','fef','cat','cat']
# print(pets)
#
# while "cat" in pets:
#     pets.remove('cat')
#
# print(pets)

# def greet_uesr(username):
#     '''显示简单的问候语句'''
#     print(f'Hello,{username}')
#
# greet_uesr("lyh")

# #位置形参
# def describe_pet(animal_type,pet_name):
#     ''' 显示宠物信息'''
#     print(f'\nI have a {animal_type}')
#     print(f"My {animal_type}'s name is {pet_name}.")
#
# describe_pet("hamster",'harry')
# #位置实参 与形参中一一对应，位置很重要
# describe_pet("dog","willie")
#
# #形参
# def describe_pet(animal_type,pet_name):
#     ''' 显示宠物信息'''
#     print(f'\nI have a {animal_type}')
#     print(f"My {animal_type}'s name is {pet_name}.")
#
# describe_pet(animal_type="hamster",pet_name='harry')
# #关键字实参，必须明确指定函数定义中的形参名
# describe_pet(pet_name="willie",animal_type="dog")

#缺省参数 这时给定形参一个默认值，输出会默认输出此值，当你调用函数时给该形参实参后，会忽略掉默认值
#使用默认形参时，必须要先在形参列表中列出没有默认值的形参，再列出有默认值的实参
# def describe_pet(pet_name,animal_type="dog"):
#     ''' 显示宠物信息'''
#     print(f'\nI have a {animal_type}')
#     print(f"My {animal_type}'s name is {pet_name}.")
#
# describe_pet(pet_name='harry')
# #此时给了默认形参传入了实参，就会输出实参的值
# describe_pet(animal_type="hamster",pet_name="willie",)

# aliens = []
# for alien_number in range(3):
#     new_alien = {'greet':"greed"}
#     aliens.append(new_alien)
#     print(f'\n{aliens}')
#     aliens = []

# #导入模块
# import socket
# #创建套接字
# # socket.SOCK_STREAM TCP
# # socket.SOCK_DGRAM  UDP
# # socket.AF_INET ipv4
# udp_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #发送数据
# # udp_socket.sendto(要发送的数据的二进制格式，对方ip和端口号)
# #参数一：要发送的数据的二进制格式  字符串转二进制格式： 字符串.encode()
# #参数二：对方ip地址和端口号 address类型 要求ip地址和端口号是一个元组  ip地址要求是字符串类型 端口号要求是整数
# udp_socket.sendto("你好".encode(),("192.168.150.30",8080))
# # 关闭套接字
# udp_socket.close()

# #导入模块
# import socket
# #创建套接字
# udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #发送数据
# udp_socket.sendto("哈哈".encode(), ("127.0.0.1",8080))
# #接收数据（二进制）
# #recvfrom(1024) 方法的作用：(每次接收1024字节)
# #       此方法会造成程序阻塞，等待另一台计算机发送来数据
# #       如果对方计算机发送来了数据 recvfrom会自动解除阻塞
# #       如果对方未发送信息 会一直等待
# recv_date = udp_socket.recvfrom(1024)
# #接收到的信息是一个元组 1）对方发来的信息的二进制 2）对方的ip地址以及端口号
# #recv_date[0]:接收到的数据的二进制
# #recv_date[1]：对方的ip地址以及端口
# #解码数据（得到字符串）
# recv_date = recv_date[0].decode("GBK")
# #输出显示接收内容
# print("来自",recv_date[1],"的消息",recv_date[0])
# #关闭套接字
# udp_socket.close()

# #导入模块
# import socket
# #创建套接字
# udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #绑定发送端端口
# # udp_socket.bind("196.168.152.65",8888)#这里是绑定自己的 ip地址可以省略 默认自己的
# local_addr = ("",8888)
# udp_socket.bind(local_addr)#这样写也可以
# #发送数据
# udp_socket.sendto("hello".encode(),('127.0.0.1',8080))#这个地方的IP和端口号是接收方的
# #关闭套接字
# udp_socket.close()
# 不管接收端还是发送端绑定端口 都是说本机作为发送端或本机作为接收端时的绑定
# 本机发送端端口绑定 其他设备接收时 都是显示一个固定端口发来
# 本机接收端口绑定 其他设备就可以通过指定接受端口 发信息到本机
# #导入模块
# import socket
# #创建套接字
# udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #绑定接收端端口
# udp_socket.bind("",8080)#这个地方的ip地址尽量写空
# #接收对方发送的数据
# recv_date,ip_port=udp_socket.recvfrom(1024)
# #recv_date = udp_socket.recvfrim(1024)
# # #解码数据
# print("接受到[%s]的消息:%s" %(str(ip_port),recv_date.decode()))
# # recv_date = recv_date[0].decode("GBK")
# # print("接受到的消息时",recv_date[0].decode(),'来自',recv_date[1])
# #输出显示
# #关闭套接字

# #导入模块
# import socket
# #创建套接字
# udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
# #设置广播权限
# udp_socket.setsockopt(socket.SOL_SOCKET,socket.SO_BROADCAST,True)
# #发送数据
# udp_socket.sendto("haha".encode(),("255.255.255.255",8080))
# #关闭套接字
# udp_socket.close()
#
# #导入模块
# import socket
# #创建套接字
# # socket.SOCK_DGRAM udp
# # socket.SOCK_STREAM tcp
# tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #建立连接 .connect(("服务器ip地址"，端口号))
# tcp_client_socket.connect(("196.128.88.12",8080))
# #发送信息 send不是sendto是因为这里面只传输内容 不需要接收方的ip地址以及端口号
# tcp_client_socket.send("我爱你".encode())
# #接收数据 recv不是recvform 是因为tcp是一对一 只接收内容 无需显示从哪个ip地址及端口发过来的信息
# recv_date = tcp_client_socket.recv(1024)
# #将接收来的二进制消息 转换为原消息 即解码数据
# recv_text = recv_date.decode()
# print(recv_text)
# #关闭套接字
# tcp_client_socket.close()

# #导入模块
# import socket
# #创建套接字
# tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #绑定端口号和IP
# tcp_server_socket.bind(("",8080))
# #开启监听(设置套接字被动模式)
# #listen()作用设置tcp_server_socket套接字为被动监听模式，不能主动发送数据
# #128 允许接受的最大连接数 在Windows中128有效 在Linux中无效
# tcp_server_socket.listen(128)
# #等待客户端连接
# #accpet()开始接受客户端连接,程序会默认进入阻塞状态(等待客户端连接)
# #当客户端连接后 会自动解除阻塞
# #recv_date数据包含两部分
# #1)返回了一个新的套接字socket  对象(为什么会返回一个新的套接字呢？)
# #因为 原套接字已经设置为了listen模式(监听)
# #当客户端与服务器收发消息时就会产生新的套接字供其使用，旧套接字会继续执行监听模式
# #2)客户端的ip地址和端口号   元组
# while True:
#     #进行拆包
#     new_client_socket,client_ip_port = tcp_server_socket.accept()
#     while True:
#         #收发数据
#         recv_date = new_client_socket.recv(1024)
#     #加入if条件判断 如果接收信息不为 空 则程序运行 如果为空则终止循环表示客户端已断开连接 服务器也要断开
#         if len(recv_date) != 0:
#             recv_text = recv_date.decode("GBK")
#             #格式化字符串
#             print("接收到[%s]的信息：%s" %(str(client_ip_port),recv_text))
#         else:
#             print("服务器断开连接")
#             break
#     #这个close关闭表示不能再和当前客户端通信
#     new_client_socket.close()
# #关闭连接 表示程序不再接收新的客户端连接 已经连接的可以
# tcp_server_socket.close()

# #导入模块
# import socket
# #创建套接字
# tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# #建立连接
# tcp_client_socket.connect(("196.168.88.252",8080))
# #接收用户输入的文件名
# file_name = input("请输入你需要下载的文件名：\n")
# #发送文件名到服务端
# tcp_client_socket.send(file_name.encode())
# #创建文件 并且准备保存
# with open("/home/demo/Desktop/"+file_name,"w") as file:
#     #接收服务端发来的数据 保存到本地(循环)
#     while True:
#         #接收文件
#         file_date = tcp_client_socket.recv(1024)
#         #判断数据是否为空 为空终止循环
#         if  file_date :
#             file.write(file_date.decode())
#         else:
#             break
# #关闭套接字
# tcp_client_socket.close()

# #导入模块
# import socket
# #创建套接字
# tcp_server_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 设置套接字地址可以重用
# # tcp_server_socket.setsockopt(当前套接字，属性名，属性值)
# # socket.SO_REUSEADDR 地址是否可以重用，True可以重用 False不可以重用
# tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
# #绑定端口
# tcp_server_socket.bind(("",8080))
# #设置监听 设置套接字由主动变为被动
# tcp_server_socket.listen(128)
# while True:
# #接收客户端连接
#     new_client_socket,tp_port = tcp_server_socket.accept()
#     #接收客户端发送的文件名
#     recv_date = new_client_socket.recv(1024)
#     file_name = recv_date.decode()
#     print(file_name)
#     try:
#         #根据文件名读取文件内容
#         with open (file_name,"rb")as file:
#         #把读取的内容发送给客户端(循环)
#             while True:
#                 #读取文件
#                 file_date = file.read(1024)
#                 #判断文件是否为空 为空终止循环
#                 if file_date:#if len(file_date) != 0:
#                     #发送文件
#                     new_client_socket.send(file_date)
#                 else:
#                     break
#     except Exception as e :
#         print("%s下载失败" % file_name)
#     else:
#         print("%s下载成功" % file_name)
#     #关闭和当前客户端的连接
#     new_client_socket.close()
# # 关闭服务器
# # tcp_server_socket.close()

# 模拟浏览器实现
# 导入模块
# import socket
# # 创建套接字
# tcp_client_socket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
# # 建立连接 web服务器默认是80端口
# tcp_client_socket.connect(("www.icoderi.com",80))
# # 拼接请求协议
# # 请求行
# # 请求头
# # 请求空行
# request_line = "GET / HTTP / 1.1\r\n"
# request_header = "Host:www.icoderi.com\r\n"
# request_blank = "\r\n"
# request_date= request_line + request_header +request_blank
# # 发送请求报文   注意 默认报文是字符串 必须转二进制
# tcp_client_socket.send(request_date.encode())
# # 接收服务器相应的内容
# recv_date = tcp_client_socket.recv(4096)
# recv_text = recv_date.decode()
# # 保存内容
# # 查询\r\n位置 find查找
# loc = recv_text.find("\r\n\r\n")
# # 截取字符串 使用字符串切片截取
# html_date = recv_text[loc+4:]
# # 保存内容到文件中
# with open("index.html","w") as file:
#     file.write(html_date)
# # 断开连接
# tcp_client_socket.close()
"""
TCP服务器
导入模块
创建套接字
设置地址重用
绑定端口
设置监听，让套接字由主动变为被动
接收客户端连接
接收客户端浏览器发送的请求协议
判断协议是否为空
拼接响应的报文
发送响应报文
关闭操作
"""
# TCP服务器
# 导入模块
# import socket
#
# def request_handler(new_client_socket,ip_port):
#     # 接收客户端浏览器发送的请求协议
#     recv_date = new_client_socket.recv(1024)
#     # 判断协议是否为空
#     if not recv_date :
#         print(f"{ip_port}客户端已下线")
#         new_client_socket.close()
#         return
#     # 根据客户端浏览器请求的资源路径，返回请求协议
#     # 1)把请求协议解码，得到请求报文的字符串
#     request_text = recv_date.decode()
#     # 2)得到请求行
#     #     查找第一个\r\n出现的位置
#     loc = request_text.find("\r\n")
#     #      截取字符串 从头开始截取 第一个\r\n出现的位置
#     request_line = request_text[:loc]
#     # 把请求行按照空格拆分 得到列表  split 按照指定字符分割字符串 返回一个列表 丢失分割字符
#     request_line_liat = request_line.split(" ")
#     # 得到请求资源路径
#     file_path = request_line_liat[1]
#     # 设置默认首页 当客户端未指定请求内容时 默认返回index。html
#     if file_path == "/":
#         file_path = "/index.html"
#     # 拼接响应的报文
#     # 响应行
#     response_line = "HTTP/1.1 200 OK\r\n"
#     # 响应头
#     response_header = "Server : Python20ws/2.1\r\n"
#     # 响应空行
#     response_blank = "\r\n"
#     # 响应主体
#     # response_body =  "Hello World"
#     #************返回固定页面***************
#     #通过with open 读取文件
#     #设置异常捕获 当客户端访问页面不存在 出现异常时
#     try:
#         with open("static"+file_path,"rb") as file :
#             response_body = file.read()
#     except  Exception as e :
#         #重新修改响应行为404
#         response_line = "HTTP/1.1 404 Not Found\r\n"
#         #响应内容为错误
#         response_body = "Error! (%s)" % str(e)
#         #把响应内容转换为字节码
#         response_body = response_body.encode()
#     # 拼接响应报文
#     response_date = (response_line + response_header +response_blank).encode() +response_body
#     # 发送响应报文
#     new_client_socket.send(response_date)
#     new_client_socket.close()
#
# def main():
#     # 创建套接字
#     tcp_server_socket  = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
#     # 设置地址重用
#     tcp_server_socket.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,True)
#     # 绑定端口
#     tcp_server_socket.bind(("",8080))
#     #设置监听，让套接字由主动变为被动
#     tcp_server_socket.listen(128)2000个字符，可以包括各国语言，特殊字符，emoji表情，链接等数据
#     # 接收客户端连接 设置调用函数
#     while True:
#         new_client_socket,ip_port = tcp_server_socket.accept()
#         request_handler(new_client_socket,ip_port)
#     # 关闭操作
#     # tcp_server_socket.close()
#
# if __name__ == "__main__":
#
#    main()
# def generate(numRows: int):
#     temp = []
#     dp = []
#
#     for i in range(0, numRows):
#         temp = [1] * (i + 1)
#         j = 1
#
#         while j < i:
#             temp[j] = dp[i - 1][j - 1] + dp[i - 1][j]
#             j += 1
#
#         dp.append(temp)
#
#     return dp
#
# generate(5)


# a = []
# a.append((1,))
# b = ['a','b','c']
# a.extend(b)
# print(a)
# c = a.index('b')
# print(c)
# a.insert(2,True)
# print(a)
# for i,j in enumerate(a):
#     if type(j)==str:
#         print(i,j)

