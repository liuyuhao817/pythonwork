#导包
import json
def read_json(filename):
    filepath = "../data/"+filename
    # 调用load方法
    with open(filepath,'r',encoding="utf-8") as f:
        return json.load(f)