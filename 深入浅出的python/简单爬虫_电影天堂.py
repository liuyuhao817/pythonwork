"""
一、定义函数，获取列表页的内容页地址 get_movie_links()
1、定义列表的地址 https://www.dytt8.net/html/gndy/dyzz/list_23_1.html
2、打开url地址，获取数据
3、解码获取到的数据
4、使用正则得到所有影片内容页地址
二、主函数main()
"""
import urllib.request
import re
def get_movie_links():
    """获取列表页的影片信息"""
    # 1、定义列表的地址 https://www.dytt8.net/html/gndy/dyzz/list_23_2.html
    film_list_url = "https://www.dytt8.net/html/gndy/dyzz/list_23_2.html"
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

    #定义一个字典用于保存我们的影片信息
    films_dict = {}

    #循环遍历url_list  同时拆包 因为返回的列表里面是元组 包含了链接和影片名两部分
    i = 1
    for content_url , file_name in url_list:
        content_url = "https://www.dytt8.net" + content_url
        print(f"影片名称{file_name},内容页地址{content_url}")
            #打开内容页
        response_content = urllib.request.urlopen(content_url)
            #接收内容页数据
            #读取网络资源
        response_concent_data = response_content.read()
        try:
                #解码 得到内容页的文本内容
            response_consent_text = response_concent_data.decode("GBK")
                #取出下载地址
            result = re.search(r"bgcolor=\"#fdfddf\"><a href=\"(.*?)\">",response_consent_text)
                # print(result.group(1))

                #字典
                #{xxx影片：xxx地址，.....}
            films_dict[file_name] = result.group(1)
            print("已经获取%d条信息" % i)
            i += 1
        except Exception as e:
            print("失败")

    return films_dict

def main():
    films_dict = get_movie_links()
    # print(films_dict)
    #把字典遍历输出
    for film_name,film_link in films_dict.items():
        print("%s | %s" % (film_name, film_link))
if __name__ == '__main__':
    main()

