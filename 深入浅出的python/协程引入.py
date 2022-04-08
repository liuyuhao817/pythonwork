# yield实现协程
# import time
#
#
# def work1():
#     while True:
#         print("正在生成")
#         yield
#         time.sleep(0.5)
#
# def work2():
#     while True:
#         print("正在生成...")
#         yield
#         time.sleep(0.5)
#
# if __name__ == "__main__":
#     w1 = work1()
#     w2 = work2()
#     while True:
#         next(w1)
#         next(w2)
#
"""
greenlet 实现协程步骤
导入模块
创建任务
创建greenlet对象
手动switch任务
"""
import time
from greenlet import greenlet

def work1():
    while True:
        print("正在生成")

        time.sleep(0.5)
        g2.switch()#切换到第二个任务

def work2():
    while True:
        print("正在生成...")

        time.sleep(0.5)
        g1.switch()#切换到第一个任务

if __name__ == "__main__":
    #创建green了他对象
    g1 = greenlet(work1)
    g2 = greenlet(work2)

    #执行work1任务
    g1.switch()