# 高级函数特性练习

## 题目1：*args 求和

def my_sum(*args):
    return sum(args)


print(my_sum(1, 2, 3))  # 期望: 6
print(my_sum(1, 2, 3, 4, 5))  # 期望: 15
print(my_sum())  # 期望: 0


## 题目2：**kwargs 打印用户信息

def user_info(**kwargs):
    # 补全：打印所有键值对
    # 格式："name: 张三", "age: 20" ...
    for key, value in kwargs.items():
        print(f"\"{key}: {value}\"")


user_info(name="张三", age=20, city="北京")

## 题目3：lambda + map 平方

nums = [1, 2, 3, 4, 5]
nums = list(map(lambda x: x ** 2, nums))
# 用 lambda 和 map 把 nums 里每个数平方
# 结果应该是 [1, 4, 9, 16, 25]
print(nums)

## 题目4：lambda + filter 找偶数

nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# 用 lambda 和 filter 找出所有偶数
# 结果应该是 [2, 4, 6, 8, 10]
nums = list(filter(lambda x: x % 2 == 0, nums))
print(nums)
## 题目5：reduce 求乘积

from functools import reduce

nums = [1, 2, 3, 4, 5]
result = reduce(lambda a, b: a * b, nums)
print(result)


# 用 reduce 计算乘积

## 题目6：递归求阶乘

def factorial(n):
    if n == 1:
        return 1
    return n * factorial(n - 1)


print(factorial(5))  # 期望: 120
print(factorial(6))  # 期望: 720


## 题目7：递归斐波那契（选做）
# 每个数是前两个数之和
def fib(n):
    #
    if n <= 2:
        return 1
    return fib(n - 1) + fib(n - 2)

# 6+5 + 5+4 + 4+3 + 3+2 + 2+1 + 1+1
print(fib(7))  # 期望: 13
print(fib(10))  # 期望: 55
