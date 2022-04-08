motorcycles=['handa','yamaha','sanling']
print(motorcycles)

motorcycles[0]='wuling'
print(motorcycles)

motorcycles.append('dayun')
#append在列表结尾添加数据
print(motorcycles)

motorcycles.insert(2,'tianqi')
#insert在指定位置添加数
print(motorcycles)

del motorcycles[2]
#del删除数据
print(motorcycles)

popped_motorcycles=motorcycles.pop()
print(motorcycles)
print(popped_motorcycles)
#删除列表最后一个数据 并返回该数据
popp_motorcycles=motorcycles.pop(1)
print(popp_motorcycles)
print(motorcycles)
#删除指定位置数据 并返回该值

motorcycles.remove('wuling')
#根据值删除元素 删除第一个符合要求的值
print(motorcycles)
motorcycles.append('wuling')
print(motorcycles)
motorcycles.append('wuling')
print(motorcycles)
motorcycles.remove('wuling')
print(motorcycles)
