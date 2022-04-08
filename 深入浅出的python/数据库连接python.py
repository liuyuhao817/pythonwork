"""
1、导入模块pymysql
2、建立连接对象 pymysql.connect()
3、创建游标对象 cursor()
4、使用游标对象执行SQL语句 execute()
5、获取执行结果 fetchall() fetchone()
6、打印输出获取的内容
7、关闭游标对象
8、关闭连接对象
"""


# # 1、导入模块pymysql
# # from pymysql import connect
# import pymysql
# # 2、建立连接对象 pymysql.connect()
# # host 主机
# # user 用户名
# # password 密码
# # database 指定数据库
# # charset 通信采用的编码方式 推荐utf8
# # port 默认为3306
# conn = pymysql.connect(host="localhost",user="root",password="123456",database="jingdong",charset="utf8")
# # 3、创建游标对象
# cur = conn.cursor()
# # 4、使用游标对象执行SQL语句
# # cur.execute(SQL语句)  返回值是影响的行数 如果是查询语句 返回值是总记录数
# result = cur.execute("select * from goods")
# print(f"查询到{result}条数据")
# # 5、获取执行结果
# # cur.fetchone() 从查询的结果中取出一条数据  返回是（）元组
# # result_list = cur.fetchone()
# result_list = cur.fetchall()#返回是((),(),(),....)
# # 6、打印输出获取的内容
# for line in result_list:
#     #line一行是一个元组
#     print(line)
# # 7、关闭游标对象
# cur.close()
# # 8、关闭连接对象
# conn.close()

# #pymysql 实现增删改
# """
# 1、导入模块
# 2、创建连接对象
# 3、创建游标对象
# 4、使用游标对象执行SQL语句
# 5、提交
# 6、获取执行结果（影响的行数）
# 7、打印执行的结果
# 8、关闭游标
# 9、关闭连接
# # """
# # 1、导入模块
# import pymysql
# # 2、创建连接对象
# conn = pymysql.connect(host="localhost",user="root",password="123456",database="jingdong")
# # 3、创建游标对象
# cur = conn.cursor()
# # 4、使用游标对象执行SQL语句
# sql = "insert into goods values(null,'老王牌',1,1,9999,1,1)"
# ret = cur.execute(sql)
# # 5、提交
# # conn.commit() 提交刚才执行的sql
# conn.commit()
# # 6、获取执行结果（影响的行数）
# # 7、打印执行的结果
# print(f"影响行数{ret}")
# # 8、关闭游标
# cur.close()
# # 9、关闭连接
# conn.cursor()

# SQL防注入
# 1、导入模块pymysql
# from pymysql import connect
import pymysql
# 2、建立连接对象 pymysql.connect()
# host 主机
# user 用户名
# password 密码
# database 指定数据库
# charset 通信采用的编码方式 推荐utf8
# port 默认为3306
conn = pymysql.connect(host="localhost",user="root",password="123456",database="jingdong",charset="utf8")
# 3、创建游标对象
cur = conn.cursor()
input_name = input("请输入你要查询的名称：\n")
params = [input_name]
# 4、使用游标对象执行SQL语句
#被注入过程分析
#input_name  = ' or 1 or '
# "select * from goods where name = '%s' order by id desc" % input_name
# "select * from goods where name = '' or 1 or '' order by id desc"
# 防止注入
# 1) 构建参数列表 params = [input_name]
# 2) 把参数传递给 execute(sql,params)
sql = "select * from goods where name = %s order by id desc"
# cur.execute(SQL语句)  返回值是影响的行数 如果是查询语句 返回值是总记录数
result = cur.execute(sql,params)
print(f"查询到{result}条数据")
# 5、获取执行结果
# cur.fetchone() 从查询的结果中取出一条数据  返回是（）元组
# result_list = cur.fetchone()
result_list = cur.fetchall()#返回是((),(),(),....)
# 6、打印输出获取的内容
for line in result_list:
    #line一行是一个元组
    print(line)
# 7、关闭游标对象
cur.close()
# 8、关闭连接对象
conn.close()