"""
生成器 是一个特殊的迭代器 (保存位置+返回下一个值)

next(迭代器) 得到下一个值
next(生成器) 也能够得到下一个值

生成器创建方式
1)列表推导式
2)函数中使用yield
"""
#
# #列表推导式
# date_list = [x*2 for x in range(10)]
# for value in date_list:
#     print(value,end=" ")
#
# #生成器的创建1
# date_list2 = (x*2 for x in range(10))
# #通过next获取下一个值
# value = next(date_list2)
# print(value) #0
# value = next(date_list2)
# print(value) #2
#
# print("----"*20)
#
# def test():
#     return 10
#
# m = test()
# print("m=",m)

#使用yield创建了一个生成器
def test1(h):
    a = 1
    b = 1
    current = 0
    while current <= h:

        data = a
        a , b = b , a+b
        current += 1
        print("--333---")
        xxx = yield data
        print("--222---")
        if xxx == 1:
            return "哈哈 我是return 我能让生成器结束"

if __name__ == "__main__":
    n = test1(5)
    m = next(n)
    print(m)
    try:
        m = next(n)
        print(m)
        n.send(1)
        print(m)
        m = next(n)
        print(m)
    except Exception as e:
        print(e)