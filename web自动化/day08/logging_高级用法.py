"""
logging日志模块四大组件
    日志器 Logger 提供了程序使用日志的入口
    处理器 Handler 将logger创建的日志记录发送到合适的目的输出
    格式器 Formatter 决定日志记录的最终输出格式
    过滤器 Filter 提供了更细粒度的控制工具来决定输出哪条日志记录，丢弃哪条日志记录
日志器（logger）是入口，真正干活儿的是处理器（handler），
处理器（handler）还可以通过过滤器（filter）和格式器（formatter）对要输出的日志内容做过滤和格式化等处理操作。
处理器：1. 控制台处理器 StreamHandler()
       2. 文件处理器 fileHandler() # 文件无限增大
       3. 根据大小切割 RotatingFileHandler()
       4. 根据时间切割 TimedRotatingFileHandler()
"""
import logging.handlers

# 获取logger    可选参数name，该参数表示将要返回的日志器的名称标识
logger = logging.getLogger("mylogger")
# 设置日志级别
logger.setLevel(logging.INFO)

# 获取控制台 处理器
sh = logging.StreamHandler()
#获取到文件 处理器
fh = logging.FileHandler("test.log",encoding="utf-8")
# TimedRotatingFileHandler()应用  根据时间切割
th = logging.handlers.TimedRotatingFileHandler(filename="./log/log02.log",
                                               when='M', #when：时间单位
                                               interval=1,#interval:时间间隔
                                               backupCount=3, #backupcount:保留的备份数量
                                               encoding="utf-8" #设置编码格式
                                              )
# 设置指定处理器的日志级别
th.setLevel(logging.ERROR)

# 添加格式器
fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
fm = logging.Formatter(fmt)

# 将格式器添加到处理器中
sh.setFormatter(fm)
fh.setFormatter(fm)
th.setFormatter(fm)

# 将处理器添加到日志器中
logger.addHandler(sh)
logger.addHandler(fh)
logger.addHandler(th)

# 输入信息
logger.info("info")
logger.debug("debug")
logger.warning("warning")
logger.error("error")
logger.critical("critical")