# 使用while循环
i = 10
while i > 0:
    print(i)
    i -= 1

# 使用while 计算 1-100之间所有偶数的和
num = 1
total = 0
while num <= 100:
    num += 1
    if num % 2 == 0:
        total += num

print(f"1-100之间所有偶数的和:{total}")

# for循环 可以跟else
msg = "hello-python"
for i in msg:
    print(i)
else:
    print("end")

# range(end) -> 从0开始循环到end结束
# range(start,end) -> 从start开始循环到end结束
# range(start,end,step) -> 从start开始,每次递进step,循环到end结束


# 计算1到100之间的奇数之和
result = 0
for i in range(1, 101):
    if i % 2 == 1:
        result += i
print(f"1到100之间的奇数之和:{result}")

# 每次递进2个,就一直是奇数
result = 0
for i in range(1, 101, 2):
    result += i
print(f"1到100之间的奇数之和:{result}")

# 计算100-500之间所有的3的倍数的数字之和
result = 0
for i in range(100, 501):
    if i % 3 == 0:
        result += i
print(f"100-500之间所有的3的倍数的数字之和:{result}")

# 打印一个长度为m, 宽为n的长方形
# print 默认输出一个回车换行 通过end参数修改为不换行
m = 12
n = 4
for i in range(n):
    for j in range(m):
        print("*", end=" ")
    print()

# 打印9*9乘法表
# 循环行数
for i in range(1, 10):
    # 1行最大为1,2行最大为2
    # 循环从1开始依次乘以行数得到
    for j in range(1, i + 1):
        print(f"{j} x {j} = {i * j}", end="\t")
    print() # 换行

# continue 和 break
for i in range(100):
    if i % 2 == 0:
        continue
    if i == 11:
        break
    print(i)

"""
1．系统随机生成一个随机数
2，用户根据提示猜数字，并将所猜的数字输入系统
3，如果猜错，系统给出提示是猜大了，还是猜小了，然后继续输入猜的数字
4，如果猜对，系统自动退出，游戏结束
"""
import random
random_number =random.randint(1,100)

while True:
    num = input("请输入一个数字: ")
    num = int(num)
    if num > random_number:
        print("你猜大了")
    elif num < random_number:
        print("你猜小了")
    else:
        print("你猜对了")
        break