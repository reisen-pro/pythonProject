# 作用域练习
# 变量的"活动范围"

## 题目1：预测输出
# 不要运行！先在脑子里想答案，再运行验证

x = 10

def change_x():
    x = 20       # 这是局部变量还是全局变量？
    print(x)     # 这里输出什么？

change_x()
print(x)         # 这里输出什么？
# 你的预测：change_x() 输出 20, 最后输出 10


## 题目2：用 global 修改全局变量

total = 0

def add_score(score):
    global total
    total += score

add_score(90)
add_score(85)
add_score(95)
print(total)     # 期望输出: 270


## 题目3：列表不需要 global

shopping_cart = []

def add_item(item):
    shopping_cart.append(item)

def remove_item(item):
    shopping_cart.remove(item)

add_item("苹果")
add_item("香蕉")
add_item("苹果")
remove_item("香蕉")
print(shopping_cart)   # 期望输出: ['苹果', '苹果']


## 题目4：作用域陷阱（进阶）

count = 0

def broken():
    # 下面这行会报错！想想为什么？
    # 取消注释运行看看报错信息
    global count
    count = count + 1
broken()
# 不运行 broken()，直接告诉我：
# 为什么 count = count + 1 会报 UnboundLocalError？
# 因为局部作用域内,count没有被定义(不知道对不对) 然后就是函数可以读取全局变量，但不能直接用 = 修改
# 怎么修复？
# 声明count为global,全局作用变量,就可以修改了
