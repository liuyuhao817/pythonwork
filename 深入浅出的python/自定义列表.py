'''
1,Mylist类
1)、初始化方法
2)、__iter__方法,对外提供迭代器
3)、addItem()方法,用于添加数据

2,自定义迭代器类 ：MyListIterator
1)、初始化方法,__init__
2)、迭代器方法,__iter__()
3)、获取下一个元素的方法,__next__()
'''
# # 1,Mylist类
# class Mylist(object):
# # 1)、初始化方法
#     def __init__(self):
#         #定义实例属性 保存数据
#         self.items = []
# # 2)、__iter__方法,对外提供迭代器
#     def __iter__(self):
#         #创建MyListIterator对象
#         mylist_iterator = MyListIteator(self.items)
#         return mylist_iterator
# # 3)、addItem()方法,用于添加数据
#     def addItem(self,data):
#         #追加保存数据
#         self.items.append(data)
#         print(self.items)
# #
# # 2,自定义迭代器类 ：MyListIterator
# class MyListIteator(object):
# # 1)、初始化方法,__init__
#     def __init__(self,items):
#         #定义实例属性 保存Mylist传递过来的items
#         self.items = items
#         #记录迭代器迭代的位置
#         self.current_index = 0
# # 2)、迭代器方法,__iter__()
#     def __iter__(self):
#         pass
# # 3)、获取下一个元素的方法,__next__()
#     #next(mylist_iterator) 就会调用__next__()方法
#     def __next__(self):
#         #1、判断当前的下标是否越界
#         if self.current_index < len(self.items):
#         #   1) 根据下标获取下标对应的元素值
#             data = self.items[self.current_index]
#         #   2) 下标位置加1
#             self.current_index += 1
#         #   3) 返回下标对应的数值
#             return data
#         # 如果越界 直接抛出异常
#         else:
#             # raise 用于主动抛出异常
#             # StopIteration 表示停止迭代
#             raise StopIteration
#
# if __name__ == "__main__":
#     mylist = Mylist()
#     mylist.addItem("张飞")
#     mylist.addItem("刘备")
#     mylist.addItem("关羽")
#     #遍历
#     #1) iter(mylist) 获取mylist对象的迭代器  ————> 会去调用Mylist ————> __iter__()
#     #2) next(迭代器) 获取下一个值
#     #3) 捕获异常
#     for value in mylist:
#         print(value)

# 1,Mylist类
class Mylist(object):
# 1)、初始化方法
    def __init__(self):
        #定义实例属性 保存数据
        self.items = []
# 2)、__iter__方法,对外提供迭代器
    def __iter__(self):
        #创建MyListIterator对象
        mylist_iterator = MyListIteator(self.items)
        return mylist_iterator
# 3)、addItem()方法,用于添加数据
    def addItem(self,data):
        #追加保存数据
        self.items.append(data)
        print(self.items)
#
# 2,自定义迭代器类 ：MyListIterator
class MyListIteator(object):
# 1)、初始化方法,__init__
    def __init__(self,items):
        #定义实例属性 保存Mylist传递过来的items
        self.items = items
        #记录迭代器迭代的位置
        self.current_index = 0
# 2)、迭代器方法,__iter__()
    def __iter__(self):
        pass
# 3)、获取下一个元素的方法,__next__()
    #next(mylist_iterator) 就会调用__next__()方法
    def __next__(self):
        #1、判断当前的下标是否越界
        if self.current_index < len(self.items):
        #   1) 根据下标获取下标对应的元素值
            data = self.items[self.current_index]
        #   2) 下标位置加1
            self.current_index += 1
        #   3) 返回下标对应的数值
            return data
        # 如果越界 直接抛出异常
        else:
            # raise 用于主动抛出异常
            # StopIteration 表示停止迭代
            raise StopIteration

if __name__ == "__main__":
    mylist = Mylist()
    #用户循环添加数据    根据自己需求
    while True:
        neirong = input("请输入你要添加的内容：")
        if len(neirong):
            mylist.addItem(neirong)
        else:
            print("输入完毕")
            break
    #遍历
    #1) iter(mylist) 获取mylist对象的迭代器  ————> 会去调用Mylist ————> __iter__()
    #2) next(迭代器) 获取下一个值
    #3) 捕获异常
    for value in mylist:
        print(value)

