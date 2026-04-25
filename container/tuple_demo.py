# 题目1： 定义一个表示日期的元组 (2026, 4, 20)，
# 用解包分别取出年、月、日并打印

my_date = (2026, 4, 20)
year, month, day = my_date
print(f"年:{year}")
print(f"月:{month}")
print(f"日:{day}")

# 题目2： 不用临时变量，交换 a=100, b=200 的值（用元组解包）

a=100
b=200
a,b = b,a
print(f"a,b: {a,b}")

# 题目3： 写一个函数 calc(a, b)，
# 同时返回两个数的 和、差、积、商，用元组解包接收4个结果并打印

def calc(x,y):
    return x+y,x-y,x*y,x/y
x = 18
y = 3
add,diff,product,quotient = calc(x,y)

print(f"和:{add}, 差:{diff}, 积:{product}, 商:{quotient}")



