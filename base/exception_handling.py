# 异常处理练习

## 题目1：基础 try/except

# 写一个函数 safe_divide(a, b)：
# - 用 try/except 处理除以零的情况
# - 正常返回 a / b
# - 捕获 ZeroDivisionError 时打印 "除数不能为0" 并返回 None
# - 捕获其他异常时打印 "发生错误: XX" 并返回 None

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("除数不能为0")
        return None


safe_divide(1, 0)


## 题目2：多个 except

# 写一个函数 parse_number(s)：
# - 尝试把字符串 s 转换成整数
# - ValueError：打印 "不是有效的整数"
# - TypeError：打印 "类型错误，需要字符串"
# - 其他异常：打印 "未知错误"

def parse_number(s):
    try:
        s = int(s)
        return s
    except ValueError:
        print("不是有效的整数")
        return None
    except TypeError:
        print("类型错误，需要字符串")
        return None
    except Exception as e:
        print(f"发生错误: {e}")
        return None


parse_number("123")
parse_number(123)
parse_number(123.0)
parse_number("abc")
parse_number([123])
parse_number(None)


## 题目3：try/except/else/finally

# 写一个函数 read_file_safe(filename)：
# - 用 with open() 打开文件
# - try: 读取内容返回
# - except FileNotFoundError: 打印 "文件不存在" 返回 None
# - else: 文件成功读取后打印 "文件读取成功"
# - finally: 打印 "操作完成"

def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            content = f.read()
    except FileNotFoundError:
        print("文件不存在")
        return None
    else:
        print("文件读取成功")
        return content
    finally:
        print("操作完成")


read_file_safe("r")


## 题目4：主动抛出异常（选做）

# 定义一个函数 validate_age(age)：
# - age 必须是整数
# - 如果 age < 0，抛出 ValueError("年龄不能为负数")
# - 如果 age > 150，抛出 ValueError("年龄不合法")
# - 否则返回 "年龄:XX"

# 再写一个函数 validate_and_double(age)：
# - 调用 validate_age(age)
# - 如果成功，返回 age * 2
# - 捕获 ValueError 并打印错误信息

def validate_age(age):
    if not isinstance(age, int):
        raise TypeError("年龄必须是整数")
    if age < 0:
        raise ValueError("年龄不能为负数")
    elif age > 150:
        raise ValueError("年龄不合法")
    else:
        return f"年龄:{age}"


def validate_and_double(age):
    try:
        result = validate_age(age)
        return age * 2
    except ValueError as e:
        print(e)
        return None


validate_and_double(10)
validate_and_double(-10)
validate_and_double(160)
