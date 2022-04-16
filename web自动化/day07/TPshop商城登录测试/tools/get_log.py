import logging

# 定义获取logging的函数
def get_logging():

    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    logging.basicConfig(level=logging.DEBUG, format=fmt, filename="../log/log1.log")
    return logging

