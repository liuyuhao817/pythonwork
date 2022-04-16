# 导包
import logging.handlers

class GetLogger:

    # 定义类属性
    logger = None

    # 定义获取logger日志器的类方法
    @classmethod
    def get_logger(cls):
        # 判断类属性logger是否还是为空，如果为空 就执行获取日志器对象等操作
        if cls.logger is None:
            # 获取 日志器
            cls.logger = logging.getLogger("mylogger")
            # 设置日志器级别
            cls.logger.setLevel(logging.INFO)
            # 获取处理器  控制台
            sh = logging.StreamHandler()
            # 获取处理器  文件  以时间分割
            th = logging.handlers.TimedRotatingFileHandler(filename="./log/log03.log",
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
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)
            """
            注意：
                1. 以上条件无论是否成立，最后都会返回类属性logger;
                2. 当第一次调用时，条件一定成立，将类属性logger设置不为空；
                3. 当第二次以上调用时，永远返回第一次设置的类属性对象；
            """
        return cls.logger

if __name__ == '__main__':
    logger = GetLogger().get_logger()
    # 输入信息
    logger.info("info")
    logger.debug("debug")
    logger.warning("warning")
    logger.error("error")
    logger.critical("critical")