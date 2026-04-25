# 字面量的写法
# 字面量 程序中直接书写的固定值(数据)
print(1)  # 整数(int)
print(3.14)  # 浮点数(float)
print(True)  # 布尔(bool)
print(False)  # 布尔(bool)
print("Hello")  # 字符串(str)
print(None)  # 空值(NoneType)

# bool本质也是整数类型(True - 1, False - 0)
print(True + 1)

# 定义变量
num: int = 123
num = 124

# python中变量可以改变类型
num = "num"

print(num)

# 定义基础数值
base_click_num: float = 20.7
# 未来两个月
month: int = 2
# 每个月的增加数
monthly_increase: int = 50

# 可以同时定义两个变量
base, total = 1, 10

# 模拟两个月的增长
print(f"初始月份: {month}")
current_click_num = base_click_num
for i in range(month):
    current_click_num += monthly_increase
    month -= 1
    print(f"第{i+1}个月后, 剩余月份: {month}, 当前数值: {current_click_num}")

print(f"最终点击数: {current_click_num}")
print(f"剩余月份: {month}")


