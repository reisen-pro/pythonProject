## 函数就是一段可以重复使用的代码。
"""
想象它是"一个盒子"：
输入 → [ 盒子 ] → 输出
好处：
写一次，用多次
代码更清晰
方便维护
"""

# 定义：def 函数名(参数):
def greet():
    print("你好！")

# 调用
greet()        # 输出：你好！
greet()        # 可以重复调用
greet()        # 不用重复写代码

## 带参数

def greet(name):  # name 是参数（输入）
    print(f"你好，{name}！")

greet("张三")  # 输出：你好，张三！
greet("李四")  # 输出：你好，李四！

## 带返回值
def add(a, b):  # 两个参数
    result = a + b
    return result  # 返回结果

sum = add(3, 5)
print(sum)  # 8
print(add(10, 20))  # 30

"""
调用：add(3, 5)
a=3, b=5
  ↓
计算 result = 8
  ↓
返回 8
  ↓
得到 sum = 8
"""