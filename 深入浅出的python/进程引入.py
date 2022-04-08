# # '''
# # 1,导入模块
# # 2,通过模块提供的Process类创建进程对象
# # 3,启动进程
# # '''
# #
# # import multiprocessing
# # import time
# # import os
# #
# # def work1(num,times):
# #     for i in range(num):
# #         print("正在运行work1....",multiprocessing.current_process(),os.getpid())
# #         #获取进程的父id
# #         print('正在运行1......',"子id",os.getpid(),"父id",os.getppid())
# #         time.sleep(times)
# #
# # if __name__ == "__main__":
# #     #获取主进程名称
# #     print(multiprocessing.current_process())
# #     #获取进程的编号 process  id
# #     # 1,multiprocessing.current_process().pid  进程编号
# #     print("主进程的编号",multiprocessing.current_process().pid)
# #     # 2,使用os模块来获取
# #     print(os.getpid())
# #     #通过模块提供的Process类创建进程对象
# #     #target 指定于进程要执行的分支函数
# #     #name 指定子进程的名称
# #     process_doj  = multiprocessing.Process(target=work1,name="p1",args=(10,),kwargs={"times":1})
# #     #启动进程
# #     process_doj.start()
# # #终端输入 kill -9 进程编号  可以终止进程
# #
# # import multiprocessing
# # import time
# # #定义全局变量
# # g_num = 0
# # #work1    对全局变量进行累加
# # def work1():
# #     global g_num
# #     for i in range(10):
# #         g_num += 1
# #     print("work1",g_num)
# # #work2    对全局变量进行读取 如果读取成功 说明可以共享
# # def work2():
# #     print("work2",g_num)
# # #定义两个进程
# # if __name__ == "__main__":
# #     t1 = multiprocessing.Process(target=work1)
# #     t2 = multiprocessing.Process(target=work2)
# #     t1.start()
# #     t2.start()
# #     time.sleep(5)
# #     print("main", g_num)
# # '''
# # 1,导入模块
# # 2,通过模块提供的Process类创建进程对象
# # 3,启动进程
# # '''
# #
# import multiprocessing
# import time
# import os
#
# def work1(num,times):
#     for i in range(num):
#         print("正在运行work1....",multiprocessing.current_process(),os.getpid())
#         #获取进程的父id
#         print('正在运行1......',"子id",os.getpid(),"父id",os.getppid())
#         time.sleep(times)
#
# if __name__ == "__main__":
#     #获取主进程名称
#     print(multiprocessing.current_process())
#     #获取进程的编号 process  id
#     # 1,multiprocessing.current_process().pid  进程编号
#     print("主进程的编号",multiprocessing.current_process().pid)
#     # 2,使用os模块来获取
#     print(os.getpid())
#     #通过模块提供的Process类创建进程对象
#     #target 指定于进程要执行的分支函数
#     #name 指定子进程的名称
#     process_doj  = multiprocessing.Process(target=work1,name="p1",args=(10,),kwargs={"times":1})
#     #进程守护
#     process_doj.daemon = True
#     #启动进程
#     process_doj.start()
#     time.sleep(2)
#     print("我要死")
#     #终止子进程
#     process_doj.terminate()
#     exit()
# #终端输入 kill -9 进程编号  可以终止进程
# """
# 队列是multiprocessing 模块提供的一个类
# 1,创建对列(指定长度)
# 2,放值
# 3,取值
# """
# import multiprocessing
# # 1,创建对列(指定长度)
# queue = multiprocessing.Queue(5)
# # 2,放值  先进先出
# # queue.put(值) 向队列里面放值
# queue.put(1)
# queue.put("helllo")
# queue.put([1,2,3])
# queue.put({"name":"ku"})
# queue.put((1,2,3))
# #队列长度为5 那么当放第六个值时，队列就进入了阻塞状态 不会报错不会结束 默认当队列取出一个值后 再被放入
# queue.put(6)
# queue.put_nowait(1245)#表示放入值 如果已满 直接报错 不等待
# # 3,取值
# #会从队列的第一个值开始取 一次取一个值 不能指定 只能顺序
# value = queue.get()
# print(value)
# #当多次取值 队列为空后 再次进入取值 会进入阻塞 等待新的数据进入队列 然后再取 程序不会报错不会继续
# queue.get_nowait()#表示取值时 若队列为空 即无值可取 就会直接报错 不会等待

'''
1,判断是否已满
2,判断是否为空
3,取出队列中消息的个数
'''
# import multiprocessing
#
# queue = multiprocessing.Queue(3)
# queue.put(1)
# queue.put(2)
# queue.put(3)
# #取值
# value = queue.get()
# # 1,判断是否已满
# # queue.full() 判断队列是否为满 返回值 True 已满 False 未满
# isFull = queue.full()
# print(isFull)
# #取值
# value = queue.get()
# # 2,判断是否为空
# isEmpty = queue.empty()#判断队列是否为空 返回值 True 空 False 非空
# print(isEmpty)
# # 3,取出队列中消息的个数
# print(queue.qsize())

# import multiprocessing
# import queue
# import time

# '''
# 1,准备两个进程
# 2,准备一个队列 一个进程向队列写入数据
# 3,另外一个进程读取数据
# '''
# import multiprocessing
# #写入数据到队列的函数
# def write_queue(queue):
#     #用for 循环向队列写入数据
#     for i in range(10):
#         #判断队列是否已满
#         if queue.full() :
#             print("队列已满")
#             break
#         queue.put(i)
#         print("成功写入")
#         time.sleep(0.5)
# #读取队列数据并显示的函数
# def read_queue(queue):
#     while True:
#         if queue.qsize == 0 :
#             print("队列已空")
#             break
#         value = queue.get()
#         print("已经读取",value)
#
# if __name__ == "__main__":
#     #创建一个空的队列
#     queue = multiprocessing.Queue(5)
#     #创建两个进程 分别写数据和读数据
#     work1 = multiprocessing.Process(target=write_queue,args=(queue,))
#     work2 = multiprocessing.Process(target=read_queue, args=(queue,))
#     work1.start()
#     #优先让写数据进行 然后进行完后 再进行读数据
#     work1.join()
#     work2.start()

# import multiprocessing
# import time
# #定义一个函数来模拟copy文件
# def copy_work():
#     print("正在拷贝文件",multiprocessing.current_process())
#     time.sleep(0.5)
#
# if __name__ == "__main__":
#     #创建一个进程池 长度3 （表示进程池中最多创建3个进程）
#     #进程池创建 两步 1 导入模块 2 创建进程池
#     pool = multiprocessing.Pool(3)
#     for i in range(10):
#        #先用进程池同步方式拷贝文件
#         # pool.apply(函数名,(传递给函数的参数1,参数2,......))
#         pool.apply(copy_work)
#         # 以进程池异步方式来拷贝文件
#        #pool.apply_async  两点注意
#         #1,pool.close() 表示不再接收新的任务
#         #2,主进程不再等待进程池执行结束后再退出 需要进程池join()
#        #        pool.join() 让主进程等待进程池执行接收后再退出
#         pool.apply_async(copy_work)
#     # pool.close()表示不再接收新的任务
#     pool.close()
#     # 主进程不再等待进程池执行结束后再退出 需要进程池join()
#     pool.join()
'''
1,准备两个进程
2,准备一个队列 一个进程向队列写入数据
3,另外一个进程读取数据
'''
import multiprocessing
import time
#写入数据到队列的函数
def write_queue(queue):
    #用for 循环向队列写入数据
    for i in range(10):
        #判断队列是否已满
        if queue.full() :
            print("队列已满")
            break
        queue.put(i)
        print("成功写入")
        time.sleep(0.5)
#读取队列数据并显示的函数
def read_queue(queue):
    while True:
        if queue.qsize == 0 :
            print("队列已空")
            break
        value = queue.get()
        print("已经读取",value)

if __name__ == "__main__":
    #创建进程池
    pool = multiprocessing.Pool(2)
    #创建进程池中的队列
    queue = multiprocessing.Manager().Queue(5)
    #使用进程池执行任务
    #两种方式 同步和异步
    # #同步方式
    # pool.apply(write_queue,(queue,))
    # pool.apply(read_queue,(queue,))
     #异步方式  两个注意 一个是让主进程等待进程池执行完毕再结束 第二个是进程池在工作后不接受新的任务
    # apply_async() 返回值 ApplyResult对象 该对象由一个wait()的方法
    #wait()  方法类似join 表示先让当前进程执行完毕 后续进程才能启动
    result = pool.apply_async(write_queue,(queue,))
    result.wait()
    pool.apply_async(read_queue,(queue,))
    pool.close()
    pool.join()
