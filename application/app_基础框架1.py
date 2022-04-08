def parse_request(recv_date):
    # 根据客户端浏览器请求的资源路径，返回请求协议
    # 1)把请求协议解码，得到请求报文的字符串
    request_text = recv_date.decode()
    # 2)得到请求行
    #     查找第一个\r\n出现的位置
    loc = request_text.find("\r\n")
    #      截取字符串 从头开始截取 第一个\r\n出现的位置
    request_line = request_text[:loc]
    # 把请求行按照空格拆分 得到列表  split 按照指定字符分割字符串 返回一个列表 丢失分割字符
    request_line_list = request_line.split(" ")
    # 得到请求资源路径
    file_path = request_line_list[1]
    # 设置默认首页 当客户端未指定请求内容时 默认返回index。html
    if file_path == "/":
        file_path = "/index.html"
    return file_path

def application(current_dir,recv_date):
    #调用函数 解析请求资源路径
    file_path = parse_request(recv_date)
    response_path = current_dir + file_path
    # 拼接响应的报文
    # 响应行
    response_line = "HTTP/1.1 200 OK\r\n"
    # 响应头
    response_header = "Server : Python20ws/2.1\r\n"
    # 响应空行
    response_blank = "\r\n"
    # 响应主体
    # response_body =  "Hello World"
    # ************返回固定页面***************
    # 通过with open 读取文件
    # 设置异常捕获 当客户端访问页面不存在 出现异常时
    try:
        with open(response_path, "rb") as file:
            response_body = file.read()
    except  Exception as e:
        # 重新修改响应行为404
        response_line = "HTTP/1.1 404 Not Found\r\n"
        # 响应内容为错误
        response_body = "Error! (%s)" % str(e)
        # 把响应内容转换为字节码
        response_body = response_body.encode()
    # 拼接响应报文
    response_date = (response_line + response_header + response_blank).encode() + response_body

    return response_date