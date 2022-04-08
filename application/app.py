

from application import utils
from application import urls
from application import funs

def parse_request(request_data, ip_port):
    """ 解析请求的报文 返回客户端请求的资源路径"""
    # 根据客户端浏览器请求的资源路径，返回请求资源
    # 1）把请求协议解码，得到请求报文的字符串
    request_text = request_data.decode()
    # 2）得到请求行
    #    （1） 查找 第一个\r\n 出现的位置
    loc = request_text.find("\r\n")
    #    （2） 截取字符串，从开头截取到 第一个\r\n 出现的位置
    request_line = request_text[:loc]
    # print(request_line)
    # 3）把请求行，按照空格拆分，得到列表
    request_line_list = request_line.split(" ")
    # print(request_line_list)

    # 得到请求的资源路径
    file_path = request_line_list[1]
    print("[%s]正在请求:%s" % (str(ip_port), file_path))

    # 设置默认首页
    if file_path == "/":
        file_path = "/index.html"

    return file_path


def application(current_dir, request_data,ip_port):

    # 调用 parse_request函数，解析请求协议，返回请求的资源路径
    file_path = parse_request(request_data, ip_port)
    # 定义变量保存资源路径
    resource_path = current_dir+file_path
    response_data = ""

    #改进动态显示
    #1、判断后缀
    if file_path.endswith(".py"):
    # 2 、让.py显示的内容和.html显示的内容分别开
    #判断请求资源路径 根据不同路径显示不同内容
    #判断 /index.py  是否在route_dict字典中出现
        if file_path in urls.route_dict:
            #根据key值 去utls.route_dict中 获取值（函数引用）
            func = urls.route_dict[file_path]
            #根据路由字典 获取函数的引用 执行该函数 返回执行的结果
            response_body = func()
            # 调用 utils 模块的 create_http_response 函数，拼接响应协议
            response_data = utils.create_http_response("200 OK", response_body.encode())

        else:
            response_body = "Sorry page not found! 404"
            # 调用 utils 模块的 create_http_response 函数，拼接响应协议
            response_data = utils.create_http_response("404 NOT FOUND", response_body.encode())


    #静态内容处理
    else:
        try:
            # 通过 with open 读取文件
            with open(resource_path, "rb") as file:
                # 把读取的文件内容返回给客户端
                response_body = file.read()

            # 调用 utils 模块的 create_http_response 函数，拼接响应协议
            response_data = utils.create_http_response("200 OK", response_body)

        except Exception as e:

            # 2）响应的内容为错误
            response_body = "Error! (%s)" % str(e)
            # 3）把内容转换为字节码
            response_body = response_body.encode()
            # 调用 utils 模块的 create_http_response 函数，拼接响应协议
            response_data = utils.create_http_response("404 Not Found", response_body)

    return response_data