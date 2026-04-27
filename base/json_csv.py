# JSON / CSV 读写练习

import json
import csv


## 题目1：JSON 序列化

# 写一个函数 save_json(data, filename)：
# - 把字典 data 保存为 JSON 文件
# - 中文用 utf-8 编码，缩进 2 空格
# 再写一个函数 load_json(filename)：
# - 读取 JSON 文件，返回字典

def save_json(data, filename):
    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


def load_json(filename):
    with open(filename, 'r', encoding='utf-8') as f:
        return json.load(f)


# 测试：
data = {'name': 'Alice', 'age': 18, 'city': '北京'}
save_json(data, 'user.json')
print(load_json('user.json'))  # {'name': 'Alice', 'age': 18, 'city': '北京'}


## 题目2：JSON 追加数据

# 写一个函数 add_user(user, filename='users.json')：
# - 读取已有数据（空文件则创建新列表）
# - 把新用户追加到列表末尾
# - 保存回文件

# 提示：
# with open(filename, 'r') as f:
#     try: data = json.load(f)
#     except: data = []

def add_user(user, filename='users.json'):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            data = json.load(f)
    except FileNotFoundError:
        data = []

    data.append(user)

    with open(filename, 'w', encoding='utf-8') as f:
        json.dump(data, f, ensure_ascii=False, indent=2)


# 测试：
add_user({'name': 'Bob', 'age': 20})
add_user({'name': 'Carol', 'age': 22})
print(load_json('users.json'))  # [{'name': 'Bob'...}, {'name': 'Carol'...}]

## 题目3：CSV 读取

# 写一个函数 read_csv(filename)：
# - 读取 CSV 文件
# - 返回列表形式的表格数据（每行是一个字典）
# - 提示：csv.DictReader

def read_csv(filename):
    try:
        with open(filename,'r',encoding='utf-8') as f:
            reader = csv.DictReader(f)
            return list(reader)
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
        return []
    except Exception as e:
        print(f"读取错误: {e}")
        return []


# # 测试用的 csv 文件内容：
# name,age,city
# Alice,18,北京
# Bob,20,上海
#
print(read_csv('test.csv'))
# # [{'name': 'Alice', 'age': '18', 'city': '北京'}, {'name': 'Bob', 'age': '20', 'city': '上海'}]


## 题目4：CSV 写入

# 写一个函数 write_csv(data, filename)：
# - data 是字典列表
# - 用 csv.DictWriter 写入
# - 字段名就是字典的 key

def write_csv(data,filename):
    try:
        # 拿到表头,key
        fieldnames = data[0].keys()
        with open(filename,'w',encoding='utf-8') as f:
            writer = csv.DictWriter(f,fieldnames=fieldnames)
            # 写入头文件,只写一次
            writer.writeheader()
            # 写入行数据
            for row in data:
                writer.writerow(row)
        print(f"成功写入 {len(data)} 条数据到 {filename}")
    except FileNotFoundError:
        print(f"文件 {filename} 不存在")
        return []
    except Exception as e:
        print(f"写入错误: {e}")
        return []

# 测试：
data = [
    {'name': 'Alice', 'age': 18},
    {'name': 'Bob', 'age': 20}
]
write_csv(data, 'output.csv')
