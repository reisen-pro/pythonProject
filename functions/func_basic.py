## 题目1：打招呼

# 定义一个函数 greet(name)
# 调用三次，分别传入"张三"、"李四"、"王五"
def greet(name):
    print(f"你好:{name}")


greet("张三")
greet("李四")
greet("王五")


## 题目2：计算器

# 定义函数 calc(a, b)
# 返回两个数的和、差、积
# 测试：calc(10, 3)
# 期望输出：和=13, 差=7, 积=30
def calc(a, b):
    return a + b, a - b, a * b


add, diff, product = calc(10, 3)
print(f"和={add}, 差={diff}, 积={product}")


## 题目3：找最大值

# 定义函数 find_max(a, b, c)
# 返回三个数中最大的那个
# 测试：find_max(5, 2, 8) → 8
def find_max(a, b, c):
    return max(a, b, c)


print(f"三个数中最大:{find_max(5, 2, 8)}")


## 题目4：判断奇偶

# 定义函数 is_even(n)
# 如果是偶数返回 True，奇数返回 False
# 测试 is_even(4) → True
# 测试 is_even(7) → False

def is_even(n):
    return n % 2 == 0
print(is_even(4))
print(is_even(7))