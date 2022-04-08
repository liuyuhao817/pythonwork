# def test():
#     print("这是一个测试")
# #函数名是一个特殊的变量 直接打印是函数保存的内存地址 调用函数就是这个函数名所代表的内存地址 然后找到函数执行
# print(test)#<function test at 0x000002A9A67DAE60>
# print(test())#这是一个测试
# #id获取对象地址
# print(id(test))#2361386774112
# #%x 获取十六进制的
# print("%x" % id(test))#255416dae60
# #1、 一个函数名是一个特殊的变量，保存了函数的地址
# print(test)#<function test at 0x000002A9A67DAE60>
# #2、自定义一个变量可以获取函数地址
# ret = test
# print(ret)#<function test at 0x00000205B567AE60>
# #3、 自定义变量调用函数：”变量名（）“
# ret()#这是一个测试

"""
* 闭包构成的条件：
  1 存在函数的嵌套关系
  2 内层函数引用了外层函数的临时变量
  3 外层函数返回内层函数的引用（地址）
"""
# def function_out(num):
#     print("function_out.......num=",num)
#     def function_in(num_in):
#         print("function_in.....num=",num)
#         print("function_in.....num_in=",num_in)
#
#     return function_in
# # function_out(10)
# #调用funtion_out获取内层函数的地址，保存到ret变量中
# ret = function_out(100)
# # 调用里层函数
# ret(88)


"""
内层定义了和外层同名的变量
  > 内层优先使用内层定义的变量，即是定义的变量的代码在内层的最后面
"""
def function_out(num):
    print("function_out.......num=",num)
    def function_in():
        #加一个 nonlocal 表示不使用内层的函数变量，而是使用函数的变量
        # 当内层存在和外层同名变量，而且内层需要使用外层定义的变量，此时应该使用关键字进行约束
        nonlocal num
        print("function_in.....num=",num)
        #内部定义的变量
        num = 88#此时会报错
    return function_in
# function_out(10)
#调用funtion_out获取内层函数的地址，保存到ret变量中
ret = function_out(100)
# 调用里层函数
ret()