# 字符串的定义方式

# 双引号定义
s1 = "hello"

# 单引号定义
s2 = 'Python'

# 三引号定义(支持多行字符串,保留换行和缩进)
s3 = """
    这是一个:
    换行的字符串
    这是最后一行
"""

print(s1, s2)
print(s3)

print(type(s1))  # <class 'str'>
print(type(s2))  # <class 'str'>
print(type(s3))  # <class 'str'>

# 转义字符
# \' 表示单引号
# \" 表示双引号
# \n 表示换行
# \t 表示制表符(相当于Tab键,通常4个空格)
msg = 'It\'s very good'  # 单引号字符串中包含单引号需要转义
MSG = "It's very good"  # 双引号字符串中包含单引号不需要转义

msg1 = "这是一个换行的句子\n这里是第二行"
msg2 = "这是一个缩进句子\t这里是缩进后的内容"

print(msg)
print(MSG)
print(msg1)
print(msg2)

# 字符串拼接
str1 = "hello"
str2 = "world"
str3 = "hello" "world"  # 字符串字面量可以直接相邻拼接
print(str1 + "," + str2)  # 使用 + 号拼接字符串变量

# 字符串与变量组合输出
name = "cc"
age = 18
pro = "软件工程"
hobby = "Java Python"

# 方法1: 使用 + 拼接(需要将数字转换为字符串)
print("大家好,我是" + name + ",今年" + str(age) + "岁,专业是" + pro + ",爱好是" + hobby)

# 方法2: 使用 % 占位符格式化
# %s - 字符串, %d - 整数, %f - 浮点数
print("大家好,我是%s,今年%d岁,专业是%s,爱好是%s" % (name, age, pro, hobby))

# 方法3: 使用 f-string (推荐,Python 3.6+)
print(f"大家好,我是{name},今年{age}岁,专业是{pro},爱好是{hobby}")
