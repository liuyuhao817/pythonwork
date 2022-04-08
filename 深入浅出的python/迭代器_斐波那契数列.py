"""
1、定义迭代器的类
2、类中必须__iter__()方法
3、类中必须__next__()方法
目标
指定生成5列的斐波那契数列
fib = Fibnacci()
    value = next(fib)
    print()
"""


class Fibnacci(object):
    def __init__(self,num):
        #定义实例属性 保存生成列数
        self.num = num
        #定义变量保存斐波那契数列的第一列和第二列
        self.a = 0
        self.b = 1
        #记录下标位置的实例属性
        self.current_index = 0
    def __iter__(self):
        #返回自己
        return self
    def __next__(self):
        #1、判断列数是否超出生成的总列数
        if self.current_index < self.num:
        #定义变量保存a的值
            data = self.a
        # a = b   b = a+b
            self.a,self.b = self.b,self.a+self.b
        # 当前列数加1
            self.current_index += 1
        # 保存a的值
            return data
        #如果超出范围 报错
        else:
            #主动抛出异常
            raise StopIteration

if __name__ == "__main__":
    #创建迭代器对象
    fib_iterator = Fibnacci(5)
    #迭代器本身又是一个可迭代对象
    for value in fib_iterator:
        print(value)

    # #next(迭代器) 得到下一个值
    # value = next(fib_iterator)
    # print(value)
    # value = next(fib_iterator)
    # print(value)
    # value = next(fib_iterator)
    # print(value)
    # value = next(fib_iterator)
    # print(value)
    # value = next(fib_iterator)
    # print(value)
    # value = next(fib_iterator)
    # print(value)

