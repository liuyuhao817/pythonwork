#导入模块
import pymysql
#创建连接对象
conn = pymysql.connect(host="localhost",user="root",password="123456",database="python_index_db")
# 创建游标对象
cur = conn.cursor()
# for循环 插入一万条数据
for i in range(10000):
    cur.execute("insert into test_index(title) values('ha-%d')" % i)
#提交数据
conn.commit()
#关闭游标
cur.close()
#关闭连接
conn.close()