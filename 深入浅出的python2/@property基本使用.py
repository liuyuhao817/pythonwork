# class Foo(object):
#
#     def __init__(self,num):
#         self.num = num
#
#     @property
#     def prop(self):
#         return self.num
# #创建对象
# foo = Foo(100)
# #调用对象方法
# # print(foo.prop())
# #foo.prop 之后 ————————>foo.prop()
# #@property 像使用属性一样去使用方法，获取值
# print(foo.prop)

"""
property其他使用
类 goods
方法：
    初始化方法
    获取价格的方法
    设置价格的方法
    删除价格的方法
"""

# class Goods(object):
#     # 初始化方法
#     def __init__(self):
#         #初始化原价
#         self.yuanjia = 1000
#         #初始化折扣
#         self.zhekou = 0.7
#
#     #获取价格的方法
#     @property
#     def jiage(self):
#         return self.yuanjia * self.zhekou
#
#     #设置价格的方法
#     @jiage.setter
#     def jiage(self,val):
#         if val > 0:
#             self.yuanjia = val
#
#     #删除价格的方法
#     @jiage.deleter
#     def jiage(self):
#         print("执行了删除")
#
# #创建对象
# goods = Goods()
# print(goods.jiage)
# goods.jiage = 500
# print(goods.jiage)
#
# #del goods.jiage == goods.jiage() 调用了delete修饰的jiage方法
# del goods.jiage


"""魔法属性和方法的使用"""
# class Goods(object):
#     """这是一个商品的类"""
#     def set_price(self):
#         """这是Goods类中定义的设置价格的方法"""
#         pass
#     def __del__(self):
#         print("正在执行删除")
# #类的描述信息
# #类名.__doc__
# print(Goods.__doc__)
#
# goods = Goods()
# #对象方法的描述
# #对象名.方法名.__doc__
# print(goods.set_price.__doc__)
#
# #获取当前模块
# print(goods.__module__)
#
# #获取对象所属的类
# print(goods.__class__)
#
# del goods


"""魔法方法和属性"""
class Goods(object):
    """这是一个商品的类"""

    #类属性
    goods_color = "白色"

    def __init__(self):
        #实例属性
        self.org_price = 100
        self.discount = 0.7

    def set_price(self):
        """这是Goods类中定义的设置价格的方法"""
        pass
    def __str__(self):
        return "我是一个寂寞的对象"

    def __call__(self, *args, **kwargs):
        print("__call__方法被调用")

    def __del__(self):
        print("正在执行删除")

    def __getitem__(self, item):
        print("key=",item)

    def __setitem__(self, key, value):
        print("key=%s,value=%s" %(key,value))

    def __delitem__(self, key):
        print("要删除key=",key )

goods = Goods()
# #对象名() 会去调用对象的__call__方法
# goods()
# #print去打印对象时 会默认输出<__main__.Goods object at 0x00000262494D29E0>
# print(goods)

# #通过__dict__获取对象信息 返回字典
# print(goods.__dict__)
# #通过__dict__获取类信息   类名.__dict__   返回值是一个字典
# print(Goods.__dict__)

#goods['a'] 调用__getitem__方法
# goods['a']
# goods['a'] = 10 调用__setitem__(self, key, value)
# goods['a'] = 10
#del goosd['a']  调用__delitem__ key
del goods['a']