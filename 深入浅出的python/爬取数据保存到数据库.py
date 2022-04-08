"""
1、定义专门的函数，负责保存数据，add_film()
    1)定义SQL，准备插入数据
    2)执行SQL语句
2、定义专门的函数，负责检测数据库中是否存在相同的数据，film_exist()
    1)定义SQL，根据名称和地址查询
    2)执行查询，并获取查询记录数
    3)如果获取的记录数>0 return True
    4)如果获取的记录数<0 return False

3、创建连接对象(全局)
4、创建游标对象(全局)
5、关闭操作

"""
import urllib.request
import re
import pymysql

def add_film(film_name,film_link):
    """保存函数"""
    # 1)定义SQL，准备插入数据
    sql = "insert into movie_link values (null,%s,%s)"
    # 2)执行SQL语句
    ret = cur.execute(sql,[film_name,film_link])
    #如果插入成功 给出提示
    if ret:
        print(f"游戏{film_name}保存成功")

def film_exist(film_name,film_link):
    """用与检测数据是否已经存在"""
    # 1)定义SQL，根据名称和地址查询
    sql = "select id from movie_link where film_name = %s and film_link = %s limit 1"
    # 2)执行查询，并获取查询记录数
    ret = cur.execute(sql,[film_name,film_link])
    # 3)如果获取的记录数 > 0 return True
    if ret:
        return True
    else:
        return False
    # 4)如果获取的记录数 < 0 return False

def get_movie_links():
    """获取列表页的游戏信息"""
    # 1、定义列表的地址 https://www.dytt8.net/html/gndy/dyzz/list_23_2.html
    film_list_url = "https://www.dytt8.net/html/newgame/index.html"
    # 2、打开url地址，获取数据
    response_list = urllib.request.urlopen(film_list_url)
    #通过read()读取网络资源数据
    response_list_data = response_list.read()
    # 3、解码获取到的数据
    response_list_text = response_list_data.decode("GBK")
    # print(response_list_text)
    # 4、使用正则得到所有影片内容页地址
    #findall 根据正则查找所有符合的字符串 返回列表
    url_list = re.findall(r"<a href=\"(.*)\" class=\"ulink\">(.*)</a>",response_list_text)
    # #保存地址 # url_list = [("/html/........","影片名"),("/html/........","影片名"),........]
    # print(url_list)#www.dytt8.net

    #定义一个字典用于保存我们的游戏信息
    films_dict = {}

    #循环遍历url_list  同时拆包 因为返回的列表里面是元组 包含了链接和影片名两部分
    i = 1
    for content_url,film_name in url_list:
        content_url = "https://www.dytt8.net" + content_url
        # print(f"游戏名称{film_name},内容页地址{content_url}")
            #打开内容页
        response_content = urllib.request.urlopen(content_url)
            #接收内容页数据
            #读取网络资源
        response_concent_data = response_content.read()
        # try:
                #解码 得到内容页的文本内容
        response_consent_text = response_concent_data.decode("GBK")
                #取出下载地址
        result = re.search(r"align=\"justify\"><a href=\"(.*?)\">", response_consent_text)
                # print(result.group(1))

                #字典
                #{xxx游戏：xxx地址，.....}
        films_dict[film_name] = result.group(1)
        print("已经获取%d条信息" % i)
        i += 1
        # except Exception as e:
        #     print("失败")

    return films_dict

def main():
    films_dict = get_movie_links()
    # print(films_dict)
    #把字典遍历输出
    for film_name,film_link in films_dict.items():
        # print("%s | %s" % (film_name, film_link))
        #如果数据存在相同数据 就不再输入
        if film_exist(film_name,film_link):
            print(f"{film_name}保存失败")
            continue
        #调用add_film方法添加数据
        add_film(film_name,film_link)

if __name__ == '__main__':
    # 3、创建连接对象(全局)
    conn = pymysql.connect(host="localhost",user="root",password="123456",database="movie_db")
    # 4、创建游标对象(全局)
    cur = conn.cursor()
    # 调用爬取数据的主函数
    main()
    #提交
    conn.commit()
    conn.close()
    cur.close()
