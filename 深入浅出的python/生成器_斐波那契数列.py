"""
1、创建一个生成器
    目标实现斐波那契数列
    1、定义变量保存第一列和第二列的值
    2、定义变量保存当前生成的位置
    3、循环生成数据  条件  当前位置的列数 小于 总列数
    4、保存a的值
    5、修改 a b 的值   a=b b=a+b
    6、返回a的值 yield

2、定义变量保存生成器
next(生成器) 得到下一个元素值
"""

# 1、创建一个生成器 目标实现斐波那契数列
def fibnacci(n):
#     1、定义变量保存第一列和第二列的值
    a = 1
    b = 1
#     2、定义变量保存当前生成的位置
    current_index = 0
#     3、循环生成数据 条件 当前位置的列数 小于 总列数
    while current_index <= n:
#     4、保存a的值
        data = a
#     5、修改a b的值 a = b b = a + b
        a,b = b,a+b
        # 列数加1
        current_index += 1
#     6、返回a的值 yield
        yield data
    #充当return作用  保存程序的运行状态 并且暂停程序执行 当下次执行时 会再从此处往下执行

if __name__ == "__main__":
# 2、定义变量保存生成
    fib = fibnacci(5)
#     next(生成器) 得到下一个元素值
    value = next(fib)
    print(value)
    value = next(fib)
    print(value)
    value = next(fib)
    print(value)
    value = next(fib)
    print(value)
    value = next(fib)
    print(value)
