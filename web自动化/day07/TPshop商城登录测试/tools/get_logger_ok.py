# 导包
import logging.handlers


class GetLogger:
    logger = None

    @classmethod
    def get_logger(cls):
        if cls.logger is None:
            # 获取 日志器
            cls.logger = logging.getLogger("mylogger")
            # 设置日志器级别
            cls.logger.setLevel(logging.INFO)
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
            cls.logger.addHandler(sh)
            cls.logger.addHandler(th)

        return cls.logger