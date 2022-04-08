import os
import threading

#拷贝函数
def copy_file(file_name,source_dir,dest_file):
    #拼接原文件路径和目标文件路径
    source_path = source_dir + "/" + file_name
    dest_path = dest_dir + "/" +file_name
    #分别打开源文件和目标文件
    with open(source_path,"rb") as source_file:
        with open(dest_path,"wb") as dest_file:
            #循环拷贝
            while True:
                data = source_file.read(1024)
                if data:
                    dest_file.write(data)
                else:
                    break



if __name__ == '__main__':
    #定义原目录和目标目录
    source_dir = "python教学视频"
    dest_dir = "/home/python/桌面/test"
    #创建目标目录
    try:
        os.mkdir(dest_dir)

    except:
        print("目标目录已存在")
    #获取原目录文件中的所有文件列表
    file_list = os.listdir(source_dir)
    #遍历列表获取需要拷贝的原文件
    for file_name in file_list:
        # copy_file(file_name,source_dir,dest_dir)
        #创建子线程 实现多任务
        sub_threading = threading.Thread(target=copy_file,args=(file_name,source_dir,dest_dir))
        sub_threading.start()