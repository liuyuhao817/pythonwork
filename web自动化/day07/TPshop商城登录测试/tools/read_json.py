#导包
import json

def read_json(filename):
    filepath = "../data/"+filename
    # 打开文件 并调用load方法
    with open(filepath,"r",encoding="utf-8") as f:
        return json.load(f)


if __name__ == '__main__':
    print(read_json("login.json"))
    """
        需求格式：[(),(),()]
        实际格式：{"":{}}
    """

    #定义一个空列表
    datas = read_json("login.json")
    arrs = []
    for data in datas.values():
        arrs.append((data["username"],data["password"],data["verify_code"],data["expect_result"],data["success"]))
    print(arrs)