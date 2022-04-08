#调用函数 socket套接字 是支持TCP/IP网络通信的基本操作单元
import socket

def send_msg(udp_socket):
    #发送消息
    #输入接收端ip地址
    ipaddr = input("请输入接收方的ip地址: \n")
    #判断是否输入为空 为空则使用默认地址
    if len(ipaddr) == 0:
        ipaddr = "127.0.0.1"
        print(f"当前的默认地址是{ipaddr}")
    #输入接收端的端口号
    port = input("请输入接收方的端口号： \n")
    #判断 是否输入为空 为空使用默认端口号
    if len(port) == 0:
        port = "8080"
        print(f"当前的默认端口号是{port}")
    #输入发送的消息
    message = input('请输入你要发送的消息: \n')
    #sendto(消息,("ip地址"，端口号)) ip地址是字符串类型 端口号是整型
    #encode编码 将发送的消息由str类型转为二进制类型
    #decode解码 将接收的消息由二进制类型转为str类型
    udp_socket.sendto(message.encode(),(ipaddr,int(port)))

def recv_msg(udp_socket):
    #接收消息
    #解包 接收到的消息包含消息以及发送方的IP地址和端口号 其中ip地址和端口号在一个元组内
    #recvfrom造成程序阻塞，当系统未接收到消息时会阻塞系统 当系统接收到消息时，会自动接触阻塞
    recv_date,ip_port = udp_socket.recvfrom(1024)
    #解码 将二进制的消息解码为str类型
    recv_text = recv_date.decode()
    #格式化输出
    print("您接收到[%s]消息是：%s" %(str(ip_port),recv_text))
#定义主函数
def main():
    #创建套接字
    #socket.AF_INET是指ipv4 socket.SOCK_DGRAM指UDP(面向无连接) SOCK_STREAM指TCP(面向有链接)
    udp_socket = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)
    #绑定端口 此处ip地址为空 会默认使用本机ip地址
    udp_socket.bind(('',8082))
    #循环菜单
    while True:
        print("************************")
        print("****** 1,发送消息 *******")
        print("****** 2,接收消息 *******")
        print("****** 3,退出系统 *******")
        print("************************")
        sum_num = int(input("请输入你要选择的序号： "))
        if sum_num == 1:
            send_msg(udp_socket)
        elif sum_num == 2:
            recv_msg(udp_socket)
        elif sum_num == 3:
            print("正在退出系统.....")
            print("退出系统")
            break
#主函数入口 当在本页面运行程序时 才会进入循环 当在其他页面运行则不成功
if __name__ == "__main__":
    main()

