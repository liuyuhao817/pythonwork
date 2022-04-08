"""
目标 给login增加一个验证功能
而且还不能修饰源代码
"""
# def function_out(func):
#     def function_in():
#         print("开始验证")
#         func()#func() = login()
#     return function_in
# @function_out
# # @function_out 装饰了login()这个函数
# # 底层：login = function_out(login)
# def login():
#     print("开始登录")
#
# #通过闭包掉用外层函数
# # login = function_out(login)
# login()#login() = function_in

"""装饰有参数的函数"""
# def function_out(func):
#     def function_in(num):
#         print("开始验证")
#         # 执行待装饰的函数 func(num) = login(num)
#         func(num)
#     return function_in
#
# #登录函数
# @function_out
# # login = function_out(login)
# def login(num):
#     print("开始登录,num=",num)
#
# login(10)


"""装饰带有可变参数的函数"""
# def function_out(func):
#     def function_in(*args,**kwargs):
#         print("开始验证")
#         print("----login:args", args)
#         print("----login:kwargs", kwargs)
#         # 执行待装饰的函数 func(num) = login(num)
#         func(*args,**kwargs)
#     return function_in
#
# #登录函数
# @function_out
# # login = function_out(login)
# def login(*args,**kwargs):
#     print("开始登录,num=")
#     print("----login:args",args)
#     print("----login:kwargs",kwargs)
#
# login(10,a=10)

"""装饰有返回值的函数"""
# def function_out(func):
#     def function_in(num):
#         print("开始验证")
#         # 执行待装饰的函数 func(num) = login(num)
#         # 如果这个地方没有return 那么login函数返回过来的值返回不出去
#         return func(num)
#     return function_in
#
# #登录函数
# @function_out
# # login = function_out(login)
# def login(num):
#     print("开始登录,num=",num)
#     return num+10 #此时返回给了func(num)中
# # login(10) = function_in(8)
# result = login(10)
# print(result)

"""通用版的装饰器"""
# def function_out(func):
#     def function_in(*args,**kwargs):
#         print("开始验证")
#         print("----login:args", args)
#         print("----login:kwargs", kwargs)
#         # 执行待装饰的函数 func(num) = login(num)
#         return func(*args,**kwargs)
#     return function_in
#
# @function_out
# #登录函数
# # login = function_out(login)
# def login(*args,**kwargs):
#     print("开始登录,num=")
#     print("----login:args",args)
#     print("----login:kwargs",kwargs)
#     return 10#此时是返回固定值
#
# result = login(10,a=10)
# print(result)


"""
在原装饰器上设置外部变量
装饰器写法：
    存在闭包
    存在待修饰的函数
"""
# def test(path):
#     print(path)
#     def function_out(func):
#         """外层函数"""
#         def function_in():
#             print("开始验证")
#             func()
#         return function_in
#     #返回装饰器和引用
#     return function_out
#
# @test("login.py")
# #@test("login.py") 分解分为两步
# #1）test("login.py") ----> function_out 引用
# #2) @ 第一步的结果  ----> @function_out
#
# #下一步：
# #login = function_out(login)
#
# #@function_out
# #login = function_out(login)
# def login():
#     print("开始登录")
#
# @test("register.py")
# def register():
#     print("开始注册")
# login()
# register()


"""
多重装饰器
创建一个装饰器，一个待装饰的函数
"""

# # 定义一个让文字加粗的装饰器
# def makeBlod(func):
#     def function_in():
#         return "<b>"+func()+"</b>"
#
#     return function_in
#
# #定义一个让文字倾斜的装饰器
# def makeItalic(func):
#     def function_in():
#         return "<i>" + func() + "</i>"
#
#     return function_in
# # <b>helloworld-1<b>
#
# @makeBlod
# # test = makeBlod(test)
# def test():
#     return "helloworld-1"
#
# @makeItalic
# def test2():
#     return "helloworld-1"
#
# @makeBlod
# @makeItalic
# def test3():
#     return "helloworld-1"
#
# print(test())#<b>helloworld-1</b>
# print(test2())#<i>helloworld-1</i>
# print(test3())#<b><i>helloworld-1</i></b>


"""
类装饰器
    作用：使用一个类为一个函数装饰
"""
# class Test(object):
#     def __init__(self):
#         print("____init_____方法")
#
#
#     def run(self):
#         print("正在奔跑")
#
#     def __call__(self, *args, **kwargs):
#         print("___call___")
#
# #创建对象
# test = Test()
# # test.run()
# #当对象名() 此时会去调用类中的__call__()方法
# test()

#类装饰器
class Test(object):
    def __init__(self,func):
        print("____init_____方法")
        print("____func____")
        #func是login的引用
        self.func = func
    def run(self):
        print("正在奔跑")

    def __call__(self, *args, **kwargs):
        print("___call___")
        print("开始验证")
        #调用原来login的内容
        self.func()

@Test
#login = Test(login)
#
def login():
    print("开始登录")

login()