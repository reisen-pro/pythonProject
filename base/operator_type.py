# 常用的数学运算符
from pickle import NONE
from re import match

num1 = 10
num2 = 3
print("-----------------常用数学运算符------------------")
print(f"{num1} + {num2} = {num1 + num2}")  # 加法
print(f"{num1} - {num2} = {num1 - num2}")  # 减法
print(f"{num1} * {num2} = {num1 * num2}")  # 乘法
print(f"{num1} / {num2} = {num1 / num2}")  # 除法(结果为浮点数)
print(f"{num1} // {num2} = {num1 // num2}")  # 整除(向下取整)
print(f"{num1} % {num2} = {num1 % num2}")  # 取余(模运算)
print(f"{num1} ** {num2} = {num1 ** num2}")  # 幂运算

# 运算符优先级: () > ** > *, /, //, % > +, -
print(1 + 3 * 4 - 10 / 2 ** 2)  # 先算2**2=4,再算10/4=2.5,然后3*4=12,最后1+12-2.5=10.5

# 获取用户输入
skip: bool = True
x = 5.0 if skip else input("请输入数字: ")
y = 3.0 if skip else input("请输入数字: ")
print(f"x 的值是{x}, y 的值是{y}")

# 将输入转换为浮点数进行计算
x_float = float(x)
y_float = float(y)

# 加法
add_result = x_float + y_float
print(f"x + y 的值是{add_result}")

# 减法
sub_result = x_float - y_float
print(f"x - y 的值是{sub_result}")

# 浮点数精度说明:
# 计算机使用二进制表示浮点数,某些十进制小数无法精确表示
# 例如: 0.1 + 0.2 != 0.3 (实际结果是 0.30000000000000004)
# 如需高精度计算,建议使用 decimal 模块

# 赋值运算符
a = 10
print("--------------------赋值运算符---------------------")
# 复合赋值运算符(先运算再赋值)
a += 5  # 等价于 a = a + 5
print(f"a += 5 的结果为:{a}")
a -= 5  # 等价于 a = a - 5
print(f"a -= 5 的结果为:{a}")
a *= 5  # 等价于 a = a * 5
print(f"a *= 5 的结果为:{a}")
a /= 5  # 等价于 a = a / 5 (结果为浮点数)
print(f"a /= 5 的结果为:{a}")
a //= 5  # 等价于 a = a // 5 (结果为整数)
print(f"a 整除 //= 5 的结果为:{a}")

# 重新赋下值,前面已经被运算过了,结果是2.0 2.0 % 3.0 看不出来效果
a = 10
a %= 3  # 等价于 a = a % 3

print(f"a 取余 %= 3 的结果为:{a}")

a = 2
a **= 3  # 等价于 a = a ** 5
print(f"a **= 3 的结果为:{a}")

print("-------------------比较运算符----------------------")

# 比较运算符

print(f"num1 == num2 ? {num1 == num2}")
print(f"num1 != num2 ? {num1 != num2}")
print(f"num1 > num2 ? {num1 > num2}")
print(f"num1 < num2 ? {num1 < num2}")
print(f"num1 >= num2 ? {num1 >= num2}")
print(f"num1 <= num2 ? {num1 <= num2}")

print("-------------------比较运算符----------------------")

# 逻辑运算符
print(f"num1 > 5 and num2 ? {num1 > 5 and num2 > 5}")
print(f"num1 > 0 or num2 > 0 ? {num1 > 0 or num2 > 0}")
print(f"not num1 == NONE ? {not num1 == NONE}")
print("-----------------------------------------")

# 键盘输入一个整数,判断这个数字是否在10-20之前
num = 15 if skip else input("请输入一个整数: ")
num = int(num)

# if 条件: 冒号下面的语句需要空格,一般是一个tab

if 10 <= num <= 20:
    print(f"{num} 在10-20之间")
else:
    print(f"{num} 不在10-20之间")

# 键盘输入一个整数,判断这个数字是基数还是偶数
num = 15 if skip else input("请输入一个整数: ")
num = int(num)
if num % 2 == 1:
    print("是奇数")
else:
    print("是偶数")

"""
根据输入的年份,判断这一年是闰年还是平年
非整百年,且能被4整除的年份是闰年
整百年份(如1900、2000年)必须被400整除才是闰年
"""

year = 2000 if skip else input("请输入年份: ")
y = int(year)
if y % 400 == 0 or (y % 100 != 0 and y % 4 == 0):
    print("是闰年")
else:
    print("是平年")

# 输入一个整数 判断它是正数负数还是0
num = 2000 if skip else input("请输入一个整数:")
num = int(num)
if num > 0:
    print("是正数")
elif num < 0:
    print("是负数")
else:
    print("是0")

# 输入三角形的边长,判断它是等边三角形,等腰三角形,普通三角形,还是不能构成三角形
num1 = 10 if skip else input("请输入边长1: ")
num2 = 10 if skip else input("请输入边长2: ")
num3 = 10 if skip else input("请输入边长3: ")
num1, num2, num3 = int(num1), int(num2), int(num3)

if (num1 + num2) > num3 and (num1 + num3) > num2 and (num2 + num3) > num1:
    if num1 == num2 == num3:
        print("你输入的是等边三角形")
    elif num1 == num2 or num1 == num3 or num2 == num3:
        print("你输入的是等腰三角形")
    else:
        print("你输入的是普通三角形")
else:
    print("你输入的边长无法构成三角形")

"""
阶梯电价规则(按总量统一计价):
1. 第一档: 2880度以下, 0.4883元/度
2. 第二档: 2880-4800度, 0.5383元/度
3. 第三档: 4800度以上, 0.7883元/度
注意: 此方式为简化计算,实际电费通常采用分段累计计价
"""

electricity_usage = 2999 if skip else input("用电量(度): ")
electricity_usage = int(electricity_usage)
unit_price = 0.4883
tier_level = 1
# 验证输入是否为正数
if electricity_usage < 0:
    print("输入错误: 用电量不能为负数")
else:
    # 根据用电量确定阶梯档次并计算电费
    if electricity_usage < 2880:
        pass
    elif electricity_usage < 4800:
        # 第二档: 中等用电
        tier_level = 2
        unit_price = 0.5383
    else:
        # 第三档: 高耗电
        tier_level = 3
        unit_price = 0.7883

    # 计算总电费
total_cost = electricity_usage * unit_price

print(f"用电量是第{tier_level}档, 电费是{total_cost:.2f}元")

# 获取星期名称
day = 3 if skip else input("请输入星期几: ")
match day:
    case "1":
        print("星期一")
    case "2":
        print("星期二")
    case "3":
        print("星期三")
    case "4":
        print("星期四")
    case "5":
        print("星期五")
    case "6" | "7":
        print("周末")
    case _:
        print("输入错误")

# 输入两个数字,根据运算符进行运算
num1 = 3 if skip else input("请输入第一个数字: ")
oper = "*" if skip else input("请输入运算符: ")
num2 = 3 if skip else input("请输入第二个数字: ")
num1, num2 = float(num1), float(num2)
match oper:
    case "+":
        print(f"{num1} + {num2} = {num1 + num2}")
    case "-":
        print(f"{num1} - {num2} = {num1 - num2}")
    case "*":
        print(f"{num1} * {num2} = {num1 * num2}")
    case "/":
        if num2 == 0:
            print("除数不能为0")
        else:
            print(f"{num1} / {num2} = {num1 / num2}")
    case _:
        print("输入错误")