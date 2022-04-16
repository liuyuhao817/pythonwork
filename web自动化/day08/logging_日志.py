"""
什么是日志
    说明：记录系统运行程序一些步骤，对一个事件(点击事件)也称为日志(Log)
特点
    1. 调试程序
    2. 定位跟踪bug
    3. 根据日志，查看系统运行是否出错；
    4. 分析用户行为，与数据统计
日志级别：是指日志信息的优先级、重要性或者严重程度
    DEBUG 调试级别，打印非常详细的日志信息，通常用于对代码的调试
    INFO 信息级别，打印一般的日志信息，突出强调程序的运行过程
    WARNING 警告级别，打印警告日志信息，表明会出现潜在错误的情形，一般不影响软件的正常使用
    ERROR 错误级别，打印错误异常信息，该级别的错误可能会导致系统的一些功能无法正常使用
    CRITICAL 严重错误级别，一个严重的错误，这表明系统可能无法继续运行
当为程序指定一个日志级别后，程序会记录所有日志级别大于或等于指定日志级别的日志信息，而不是仅仅记录指定级别的日志信息；
    一般建议只使用DEBUG、INFO、WARNING、ERROR这四个级别
提示：
    1. 开发常用以上 debug、info、warning、error
    2. 测试常用级别：info、error
"""
import logging

"""
如何选择日志级别
在开发环境和测试环境中，为了尽可能详细的查看程序的运行状态来保证上线后的稳定性，
    可以使用DEBUG或INFO级别的日志获取详细的日志信息，这是非常耗费机器性能的。
在生产环境中，通常只记录程序的异常信息、错误信息等（设置成WARNING或ERROR级别），
    这样既可以减小服务器的I/O压力，也可以提高获取错误日志信息的效率和方便问题的排查。
"""
# 设置日志级别 DEBUG < INFO < WARNING < ERROR < CRITICAL
# logging中默认的日志级别为 logging.WARNING
# 设置日志格式
# 默认的日志的格式为： 日志级别:Logger名称:日志内容  如：DEBUG:root:这是一条debug信息
# %(asctime)s: 打印日志的时间  如：2018-01-01 12:00:00
# %(levelname)s: 打印日志级别名称
# %(message)s: 打印日志信息
# %(name)s Logger的名字
# %(filename)s 调用日志输出函数的模块的文件名
# %(funcName)s 调用日志输出函数的函数名
# %(lineno)d 调用日志输出函数的语句所在的代码行
fmt = '%(asctime)s %(levelname)s [%(name)s] [%(filename)s(%(funcName)s:%(lineno)d)] - %(message)s'
logging.basicConfig(level=logging.INFO, format=fmt,filename="./log/log01.log")
"""
level  设置日志级别
format   设置日志格式
filename  将日志信息输出到文件中
"""
# 2022-04-15 12:02:34,907 INFO [root] [logging_日志.py(<module>:55)] - 这是一条info信息

logging.debug("这是一条debug信息")
logging.info("这是一条info信息")
logging.warning("这是一条warning信息")
logging.error("这是一条error信息")
logging.critical("这是一条critical信息")