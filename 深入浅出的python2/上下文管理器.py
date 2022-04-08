"""
类方法实现上下文管理器
类：MyFile
类方法：
    __enter__() 上文方法
    __exit__()  下文方法
    __init__  接收参数并且初始化

"""
#
# class MyFile(object):
#
#     #__enter__() 上文方法
#     def __enter__(self):
#         print("进入上文")
#         #打开文件
#         self.file = open(self.file_name,self.file_model)
#         #返回打开的文件资源
#         return self.file
#
#     #__exit__()  下文方法
#     def __exit__(self, exc_type, exc_val, exc_tb):
#         print("进入下文")
#         #关闭文件资源
#         self.file.close()
#
#     #__init__  接收参数并且初始化
#     def __init__(self,file_name,file_model):
#         """保存文件名和文件打开方式到实例属性中"""
#         self.file_name = file_name
#         self.file_model = file_model
#
#
# if __name__ == '__main__':
#     with MyFile("hello.txt","r") as file:
#         #开始读取文件
#         file_data = file.read()
#         print(file_data)


"""
装饰器实现上下文管理器
思路：
    def myopen(file_name,file_model):
        上文（打开资源）
        yield
        下文（关闭资源）
        
装饰器装饰函数的步骤
    导入模块 from contextlib import contextmanager
    开始装饰
"""

from contextlib import contextmanager

@contextmanager
def myopen(file_name,file_model):
    print("进入上文")
    #打开文件
    file = open(file_name,file_model)
    #返回资源
    yield file
    print("进入下文")
    #下文
    #关闭文件
    file.close()


with myopen("hello.txt","r") as file:
    file_data = file.read()
    print(file_data)