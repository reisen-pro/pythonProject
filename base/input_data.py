# input() 函数获取用户输入,返回的都是字符串类型
name = input("请输入你的姓名: ")
age = input("请输入你的年龄: ")
print(f"您的姓名是:{name},年龄是:{age}")

# 模拟ATM取款
money = 10000
password = input("请输入密码: ")
put_money = input("请输入取款金额: ")

# 将输入的字符串转换为整数进行计算
money = money - int(put_money)
print(f"取款成功,余额为:{money}")

