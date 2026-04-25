## 题目1：默认参数

# 定义函数 power(base, exponent=2)
# 功能：计算 base 的 exponent 次方
# 默认 exponent=2，就是算平方
# 测试：power(3) → 9
# 测试：power(2, 3) → 8
def power(base, exponent=2):
    return base**exponent

print(power(3))
print(power(2,3))

## 题目2：打印个人信息

# 定义函数 info(name, age=18, city="未知")
# 用一句话打印个人信息
# 测试：info("张三") → "张三，18岁，来自未知"
# 测试：info("李四", 20, "北京") → "李四，20岁，来自北京"
def info(name, age=18, city="未知"):
    print(f"{name},{age}岁,来自{city}")
info("张三")
info("李四", 20, "北京")

## 题目3：返回None的判断

# 定义函数 find_and_print(name, names_list)
# 在列表里找名字，找到打印"找到了"，没找到打印"没找到"
# 函数只打印，不返回值
# 测试：find_and_print("张三", ["李四", "王五"]) → 没找到
# 测试：find_and_print("王五", ["李四", "王五"]) → 找到了

def find_and_print(name, names_list):
    print(f"{'找到了' if name in names_list else '没找到'}")
find_and_print("张三", ["李四", "王五"])
find_and_print("王五", ["李四", "王五"])