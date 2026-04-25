## 字典
# 列表用数字索引找元素，字典用名字（键）找元素：

# 列表：只能用数字找
student = ["张三", 18, "北京"]
print(student[0])  # "张三"  ← 你得记住0是名字

# 字典：用名字找，一目了然
student = {"name": "张三", "age": 18, "city": "北京"}
print(student["name"])  # "张三"  ← 直接用名字取
print(student["age"])  # 18




## 基本操作

# 创建
person = {"name": "张三", "age": 18}

# 读取
print(person["name"])           # "张三"
print(person.get("age"))        # 18
print(person.get("phone", "无")) # "无" ← 键不存在时返回默认值，不报错

# 添加 / 修改（一样的写法）
person["city"] = "北京"         # 添加新键
person["age"] = 19              # 修改已有键

# 删除
del person["city"]

# 遍历
for key in person:
    print(key, person[key])

for key, value in person.items():   # 更推荐这种
    print(f"{key}: {value}")

## 字典嵌套（重要！）

# 字典里套字典
students = {
    "张三": {"语文": 85, "数学": 90},
    "李四": {"语文": 72, "数学": 95}
}

# 取张三的数学成绩
print(students["张三"]["数学"])