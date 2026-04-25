##题目1：个人信息管理

# 创建一个字典存储你自己的信息（名字、年龄、城市、爱好列表）
# 打印每一项信息
# 修改年龄 +1
# 添加一个新字段 "email"
# 删除 "city" 字段
# 最后打印完整字典

person = {
    "name": "张三",
    "age": 20,
    "city": "Jiangsu",
    "hoppy": "study"
}
# 打印每一项信息
for key, value in person.items():
    print(f"{key} : {value}")

person["age"] = person["age"] + 1  # 修改年龄 +1
person["email"] = "1234@qq.com"
del person["city"]

for key, value in person.items():
    print(f"{key} : {value}")

## 题目2：词频统计

text = "apple banana apple orange banana apple"
# 统计每个单词出现的次数
# 期望输出: {'apple': 3, 'banana': 2, 'orange': 1}
# 提示：先 split() 拆成列表，再用字典统计
text_list = text.split(" ")
text_obj = {}

# text_obj.get(key,default = )
# 直接获取没有过的key的数据时,会报错 通过get函数可以通过返回一个默认值,可以直接获取

# for text in text_list:
#     text_obj[text] = text_obj.get(text,0) + 1

# 这里用了collections模块里面的计数器
#  collections 模块提供了一些非常有用的数据结构
#  比如 namedtuple（命名元组），以及常用的 Counter（计数器）、defaultdict（默认字典）等。
from collections import Counter

text_obj = Counter(text.split())

for key, value in text_obj.items():
    print(f"{key}出现的次数是: {value}")

## 题目3：成绩系统升级版

# 用字典存储3个学生的语文、数学、英语成绩
# 计算每个学生的平均分
# 找出平均分最高的学生

students = {
    "张三": {"语文": 88, "数学": 73, "英语": 91},
    "李四": {"语文": 95, "数学": 84, "英语": 88},
    "王五": {"语文": 91, "数学": 85, "英语": 88}
}
## 原先方法,分两个步骤,先获取平均分 通过 总分 sum / 数量count 得到平均分
score_avg = {}
for key, value in students.items():
    score_count = 0
    score_sum = 0
    for name, score in value.items():
        score_sum = score_sum + score
        score_count += 1
    score_avg[key] = score_sum / score_count

## 然后对数据进行处理,输出平均分和得到最高分和
score_max = 0
score_max_name = ""
for key, value in score_avg.items():
    if score_max < value:
        score_max = value
        score_max_name = key
    print(f"学生:{key}:的平均分为:{value}")

# values() 取所有值，配合 sum() 和 len()
for key, value in students.items():
    scores = value.values()  # dict_values([88, 73, 91])
    avg = sum(scores) / len(scores)  # 一行搞定！
    score_avg[key] = avg
    print(avg)

best = max(score_avg,key=score_avg.get)
print(f"平均分最高的是：{best}，{score_avg[best]:.1f}分")
print(f"学生:{score_max_name}:的平均分最高,是:{score_max}")
