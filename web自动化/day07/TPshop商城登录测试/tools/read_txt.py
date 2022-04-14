def read_txt(filename):
    filepath = "../data/"+filename

    with open(filepath,"r",encoding="utf-8") as f:
        # readlines 作为列表返回文件中的所有行，其中每一行都是列表对象中的一项
        return f.readlines()


if __name__ == '__main__':
    datas = read_txt("login.txt")

    arrs = []
    for data in datas:
        # strip() 方法用于移除字符串头尾指定的字符（默认为空格或换行符）或字符序列。
        # split() 通过指定分隔符对字符串进行切片 返回值是列表
        arrs.append(tuple(data.strip().split(",")))
    print(arrs)