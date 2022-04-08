def create_http_response(status,response_body):
    # 拼接响应的报文
    # 响应行
    response_line = "HTTP/1.1 %s\r\n" %status
    # 响应头
    response_header = "Server : Python20ws/2.1\r\n"
    #服务器响应头加这句话 表明浏览器优先使用html解析服务器返回的内容
    response_header += "Content-Type: text/html\r\n"
    # 响应空行
    response_blank = "\r\n"
    # 响应主体
    response_date = (response_line + response_header + response_blank).encode() + response_body

    return response_date