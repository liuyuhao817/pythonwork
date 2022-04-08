"""
定义若干函数实现不同功能
1、index()
2、center()
3、gettime()

装饰器路由：
    装饰器工厂
    待装饰函数
    在装饰器内部把路径添加到字典中

"""

import time
from application import urls
import re
import pymysql

def route(path):
    #path 向装饰器内部传递参数 path  /index.py
    #装饰器
    #字典
    #{"index.py":index函数引用}
    def functio_out(func):

        urls.route_dict[path] = func

        def function_in():
            return func
        return function_in()

    return functio_out

@route("/index.py")
def index():
    """处理index.py请求"""
    #1、打开文件
    with open("深入浅出的python/templates/index.html") as file:
    #2、读取文件内容
        content = file.read()
    #数据库查询
    #导入模块
    #创建连接
        conn = pymysql.connect(host="localhost",user="root",password="123456",database="shock_db")
    #创建游标对象
        cur = conn.cursor()
    #通过游标执行查询
        cur.execute("select * from info")
    #获取查询的结果
        # data_from_mysql = str(cur.fetchall())
        data_from_mysql = ""
    #1、遍历元组 得到每一行信息
        for line in cur.fetchall():
            str = """<tr>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td>%s</td>
                    <td><input type="button" value="添加" id="toAdd" name="toAdd" systemidvaule="000007"></td>
                </tr>
                """ % line
            data_from_mysql += str
    #2、拼接html格式的字符串
    #关闭操作
    #先关闭游标 再关闭连接
        cur.close()
        conn.close()
        #导入正则模块
        #使用正则替换
        content = re.sub("{%content%}",data_from_mysql,content)
    #3、返回文件内容
    return content

@route("/center.py")
def center():
    """处理center.py请求"""
    # 1、打开文件
    with open("深入浅出的python/templates/center.html") as file:
        # 2、读取文件内容
        content = file.read()
        # 导入模块
        # 创建连接
        conn = pymysql.connect(host="localhost", user="root", password="123456", database="shock_db")
        # 创建游标对象
        cur = conn.cursor()
        # 通过游标执行查询
        cur.execute("select i.code,i.short,i.chg,i.turnover,i.price,i.highs,f.note_info from info i , focus f where i.id = f.id")
        # 获取查询的结果
        # data_from_mysql = str(cur.fetchall())
        data_from_mysql = ""
        # 1、遍历元组 得到每一行信息
        for line in cur.fetchall():
            str = """
            <tr>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td>%s</td>
                <td><a type="button" class="btn btn-default btn-xs" href="/update/000007.html"> <span class="glyphicon glyphicon-star" aria-hidden="true"></span> 修改 </a></td>
                <td> <input type="button" value="删除" id="toDel" name="toDel" systemidvaule="000007"></td>
            </tr>
            """ % line
            data_from_mysql += str
        # 导入正则模块
        # 使用正则替换
        content = re.sub("{%content%}", data_from_mysql, content)
    return "This is center show"

@route("/gettime.py")
def gettime():
    """处理gettime.py请求"""

    return "This is gettime show %s" % time.ctime()