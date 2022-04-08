# import time
# import threading
# #唱歌函数
# def sing():
#
#         print("正在唱歌....")
#         time.sleep(1)
#
# # #跳舞函数
# def dance():
#
#         print("正在跳舞....")
#         time.sleep(0.5)
#
# if __name__ == "__main__":
#     for i in range(5):
#         porject = threading.Thread(target=sing)
#         porject.start()
#         project2 = threading.Thread(target=dance)
#         project2.start()
# #单线程
# import time
#
# def saySorry():
#     print("对不起我错了")
#     time.sleep(10)
#
# if __name__ == "__main__" :
#     for i in range(5) :
#         saySorry()

'''
子线程创建步骤
导入模块 threading
使用threading.Thread() 创建对象(子线程对象)
指定子线程执行的分支
启动子线程 线程对象.start()
'''
# import time
# import threading
#
# def saySorry():
#     print("对不起我错了")
#     time.sleep(1)
#
# if __name__ == "__main__" :
#     # 子线程创建步骤
#     # 导入模块threading
#     for i in range(5) :
#         # 使用threading.Thread()创建对象(子线程对象)
#         # 指定子线程执行的分支
#         # threading.Thread(target=函数名)
#         thread_obj = threading.Thread(target=saySorry)
#
#         # 启动子线程 线程对象.start()
#         #线程只有调用start才能执行
#         thread_obj.start()

# import time
# import threading
# #唱歌函数
# def sing():
#     for i in range(5):
#         print("正在唱歌....",threading.current_thread())#<Thread(Thread-1, started 19024)>
#         time.sleep(1)
#
# # #跳舞函数
# def dance():
#     for i in range(5):
#         print("正在跳舞....",threading.current_thread())#<Thread(Thread-2, started 7232)>
#         time.sleep(0.5)
#
# if __name__ == "__main__":
#     #线程的名称 threading.current_thread()  当前的线程对象 对象中含有名称
#     print(threading.current_thread())#v<_MainThread(MainThread, started 416)>
#
#     #threading.enumerate() 可以获取当前活跃的线程数量
#     threading_list = threading.enumerate()
#     print("当前线程数量",len(threading_list))#1 因为现在只有一个1主线程
#
#     porject = threading.Thread(target=sing)
#     project2 = threading.Thread(target=dance)
#     # threading.enumerate() 可以获取当前活跃的线程数量
#     # threading_list = threading.enumerate()
#     print("当前线程数量", len(threading_list))#1 因为现在多线程还未启动 start()
#
#     porject.start()
#     project2.start()
#         #通过循环打印线程数量 观察线程变化
#     while True:
#         # threading.enumerate() 可以获取当前活跃的线程数量
#         threading_list = threading.enumerate()
#         print("当前线程数量", len(threading_list))#3 此时 由主线程和两个子线程
#         if len(threading_list) <= 1:
#             break
#         time.sleep(1)

# import time
# import threading
#
#
# def sing(a,b,c):
#     print("参数",a,b,c)
#     for i in range(5):
#         print("singing.......")
#         time.sleep(1)
#
#
# def dunce():
#     for i in range(5):
#         print("dunceing........")
#         time.sleep(1)
#
#
# if __name__ == "__main__":
#     # 在线程中传递参数有三个方法
#     # 1,使用元组传递 threading.Thread(target=xxx,args=(参数1,参数2,参数3....))
#     # project = threading.Thread(target=sing, args=(10, 100, 1000))
#     # 2,使用字典传递 threading.Thread(target=xxx,kwargs={参数名:参数值,.....})
#     # project = threading.Thread(target=sing,kwargs={"a":10,"c":1000,"b":100})
#     # 3,混合使用元组和字典 threading.Thread(target=xxx,args=(参数1,参数2,参数3....),kwargs={参数名:参数值,.....})
#     #注意 这个方式 第一个元组传的一定是第一个参数 注意顺序 字典因为是键值对 所以只要名称对上就好 无关顺序
#     #字典可以给指定参数传值 而元组只能顺序传值 字典传可变参数 元组传固定参数
#     project = threading.Thread(target=sing,args=(10,),kwargs={"c": 1000, "b": 100})
#     project1 = threading.Thread(target=dunce)
#
#     project.start()
#     project1.start()
# import threading
# import time
#
# def work1():
#     for i in range(10):
#         print("正在执行work1.....")
#         time.sleep(1)
#
# if __name__ == "__main__":
#     thread_work = threading.Thread(target=work1)
#
#     # 线程守护 子线程守护主线程 即当主线程结束后 子线程也随之结束
#     # setDaemon(True) 表示子线程守护主线程
#     thread_work.setDaemon(True)
#     thread_work.start()
#     #睡眠两秒
#     time.sleep(2)
#     print("over")
#     #让程序退出 主线程结束
#     exit()
#     #以上情况就是主线程在我们主动退出后 子线程仍在运行

# '''
# 1，让自定义类继承 threading.Thread 类
# 2，重写父类(threading.Thread) run方法
# 3，通过创建子类对象 让子类对象.start() 就可以启动子线程
#
# '''
#
# import threading
# import time
#
# # 自定义线程类 类名：MyThread
# class MyThread(threading.Thread):
#
#     def __init__(self,num):
#         #super 先去调用父类的__init__方法 不然子类重写__init__后 系统会默认使用子类新写的
#         super().__init__()
#         self.num = num
#     # 重写父类的run方法
#     def run(self):
#         for i in range(5):
#             #self.name 也是从父类继承的一个属性
#             print("正在执行子线程run方法......",i,self.name,self.num)
#             time.sleep(1)
#
# if __name__ == "__main__":
#     #创建对象
#     mythread = MyThread(10)
#     #线程对象.start() 启动线程
#     #子类从父类继承了start()方法
#     mythread.start()
#     print("xxxxxxx")
#
# import threading
# import time
#
# g_num = 0
#
# def work1():
#     #申明g_num为全局变量
#     global g_num
#
#     for i in range(1000000):
#         g_num += 1
#     print("work1.........",g_num)#10
#
# def work2():
#     # 申明g_num为全局变量
#     global g_num
#
#     for i in range(1000000):
#         g_num += 1
#     print("work2.........",g_num)#  g_num可以在多个线程中共享
# #结论 当多个线程修改同一变量时 会出现资源竞争 导致结果有误
# if __name__ == "__main__":
#     #创建两个子线程
#     t1 = threading.Thread(target=work1())
#     t2 = threading.Thread(target=work2())
#
#     #启动俩个子线程
#     t1.start()
#     #让t1优先执行 t1执行完后 t2才执行
#     t1.join()
#     t2.start()
#     # #循环睡眠 保证 最后打印的print 是在上面两个子线程运行完后执行的
#     # while len(threading.enumerate()) != 1:
#     #     time.sleep(1)
#     # #在t1 t2 执行完后 再打印g_num
#     # print("main..........",g_num)

'''
1,创建一把互斥锁
2,在使用资源前锁定资源
3,使用完资源后解锁资源
'''
# import threading
# import time
#
# g_num = 0
#
# def work1():
#     #申明g_num为全局变量
#     global g_num
#     #上锁
#     lock1.acquire()
#     for i in range(1000000):
#
#         g_num += 1
#      #解锁
#     lock1.release()
#     print("work1.........",g_num)#10
#
# def work2():
#     # 申明g_num为全局变量
#     global g_num
#     # 上锁
#     lock1.acquire()
#     for i in range(1000000):
#
#         g_num += 1
#     #解锁
#     lock1.release()
#     print("work2.........",g_num)#  g_num可以在多个线程中共享
# #结论 当多个线程修改同一变量时 会出现资源竞争 导致结果有误
# if __name__ == "__main__":
#     #创建一把互斥锁
#     lock1 = threading.Lock()
#     #创建两个子线程
#     t1 = threading.Thread(target=work1())
#     t2 = threading.Thread(target=work2())
#
#     #启动俩个子线程
#     t1.start()
#     # #让t1优先执行 t1执行完后 t2才执行
#     # t1.join()
#     t2.start()
#     #循环睡眠 保证 最后打印的print 是在上面两个子线程运行完后执行的
#     while len(threading.enumerate()) != 1:
#         time.sleep(1)
#     #在t1 t2 执行完后 再打印g_num
#     print("main..........",g_num)

# import threading
# #定义函数 根据下标获取列表元素值
# def get_value(index):
#
#     date_list = [1,3,5,7,9]
#     #上锁
#     lock1.acquire()
#
#     #判断下标是否合法
#     if index >= len(date_list):
#         print("下标越界",index)
#
#         # lock1.release()  #在这加锁后 若未进行解锁 就会进入死锁 有加锁要进行解锁
#         return
#     print(date_list[index])
#     #解锁
#     lock1.release()
#
#
# #创建10个线程 观察资源等待状态
# if __name__ == "__main__":
#     #创建一把锁
#     lock1 = threading.Lock()
#     #循环创建10个线程
#     for i in range(10):
#         t1 = threading.Thread(target=get_value,args=(i,))
#         t1.start()