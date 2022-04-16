import json

def read_json(file_name):
    file_path = "../data/" + file_name

    with open(file_path,'r',encoding='utf-8') as f:
        json_data = json.load(f)
        return json_data

if __name__ == '__main__':
    # print(read_json('login.json'))
    datas = read_json('login.json')
    arrs = []
    for data in datas.values():
        arrs.append((data["username"], data["password"], data["verify_code"], data["expect_result"], data["success"]))
    print(arrs)