'''
1 定义变量 保存源文件夹 目标文件夹所在的位置
2 在目标路径创建新的文件夹
3 获取源文件夹中的所有文件（列表）
4 遍历列表 得到所有的文件名
5 定义函数 进行文件拷贝
文件拷贝函数 ：
参数：源文件夹路径 目标文件夹路径 文件名
    1 拼接源文件和目标文件的具体路径
    2 打开源文件 创建目标文件
    3 读取源文件内容 写入到目标文件夹中 （while）
'''
import os
import multiprocessing

def copy_work(source_dir,dest_dir,file_name):
    """ 根据参数 拷贝文件 """
    # 1 拼接源文件和目标文件的具体路径
    # D:\python_heima_shipk\mast\1.txt ----> C:\Users\lyh\Desktop\mast\1.txt
    # 2 打开源文件 创建目标文件
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" + file_name

    # 3 读取源文件内容 写入到目标文件夹中 （while ）
    with open(source_path,"rb") as source_file:
        #创建目标文件
        with open(dest_path,"wb") as dest_file:
            #循环读取
            while True:
                #读取源文件 保存到目标文件
                file_date = source_file.read(1024)
                #判断文件是否读取完毕
                if file_date:
                    dest_file.write(file_date)
                else:
                    break


if __name__ == "__main__":
    print(multiprocessing.current_process())
    # 1定义变量 保存源文件夹目标文件夹所在的位置
    source_dir = "./txst"
    dest_dir = "/home/lyh/Desktop/test"
    # 2在目标路径创建新的文件夹
    try:
        os.mkdir(dest_dir)#在指定位置创建文件夹
    except Exception as e:
        print("文件已经存在")
        # 3获取源文件夹中的所有文件（列表）
    file_list = os.listdir(source_dir)
        # 4遍历列表得到所有的文件名
    #创建进程

    pool = multiprocessing.Pool(3)
    for file_name in file_list:
        # 5定义函数 进行文件拷贝
        pool.apply_async(copy_work,(source_dir,dest_dir,file_name))

    pool.close()
    pool.join()
