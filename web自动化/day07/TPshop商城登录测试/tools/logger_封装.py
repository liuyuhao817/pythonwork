# 导包
import logging.handlers

def get_logger():
    # 获取 日志器
    logger = logging.getLogger("mylogger")
    # 设置日志器级别
    logger.setLevel(logging.INFO)
    # 获取处理器  控制台
    sh = logging.StreamHandler()
    # 获取处理器  文件  以时间分割
    th = logging.handlers.TimedRotatingFileHandler(filename="../log/log01.log",
                                                   when="midnight",
                                                   encoding="utf-8",
                                                   interval=1,
                                                   backupCount=3
                                                   )
    # 设置指定处理器的日志级别
    th.setLevel(logging.ERROR)
    # 设置格式器
    fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
    fm = logging.Formatter(fmt)

    # 将格式器设置到控制台处理器中
    sh.setFormatter(fm)

    # 将格式器设置到文件处理器中
    th.setFormatter(fm)

    # 将处理器添加到日志器
    logger.addHandler(sh)
    logger.addHandler(th)

    return logger

if __name__ == '__main__':
    logger = get_logger()
    # 输入信息
    logger.info("info")
    logger.debug("debug")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")