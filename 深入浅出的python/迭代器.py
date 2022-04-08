#可迭代对象
date_list = [1,3,5,7,9]

#获取迭代器
li_iterator = iter(date_list)

#根据迭代器 可以获取下一个元素
value = next(li_iterator)
print(value)  #1
value = next(li_iterator)
print(value)  #3
value = next(li_iterator)
print(value)  #5
value = next(li_iterator)
print(value)  #7
value = next(li_iterator)
print(value)  #9
value = next(li_iterator)
print(value)  #异常：StopIteration

#自定义迭代器类 满足两点
#1,必须含有__iter__()
#2,必须含有__next__()
class MyIterator(object):
    def __iter__(self):
        pass
    #当next(迭代器)时 会自己调用这个方法
    def __next__(self):
        pass
