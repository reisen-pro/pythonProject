# 元组和列表很像，最大的区别只有一个：元组不能修改！

# 列表 - 可以改
my_list = [1, 2, 3]
my_list[0] = 99  # ✅ 没问题

# 元组 - 不能改
my_tuple = (1, 2, 3)
# my_tuple[0] = 99     # ❌ TypeError！

"""
为什么需要不能改的东西？
    坐标：(x, y) 不应该被随便改
    RGB颜色：(255, 0, 0) 红色，改了就不是红色了
    函数返回多个值：return (成功, 数据) 打包返回
    字典的键：列表不能当字典的键，元组可以
"""

## 元组的写法

t1 = (1, 2, 3)  # 普通元组
t2 = 1, 2, 3  # 括号可以省略
t3 = (42,)  # ⚠️ 单元素元组必须加逗号！
t4 = (42)  # ❌ 这不是元组，这只是数字42加了括号

print(type(t3))  # <class 'tuple'>
print(type(t4))  # <class 'int'>

## 元组解包（最常用！）
point = (10, 20)
x, y = point  # 解包！x=10, y=20

# 交换变量
a, b = 1, 2
a, b = b, a  # 本质就是元组解包


# 函数返回多个值
def get_info():
    return "张三", 18, "北京"  # 返回元组


name, age, city = get_info()  # 解包接收

# (*)扩展解包 *代表多个占位符 处理不确定数量的元素
name,*info = get_info()
print(name)
print(*info)

t5 = (1.0, 4.0, 56.444, 78.0, 1.0, 3.0, 4,3.3333)
# count 元素出现的次数
print(t5.count(1))
# index 元素出现的索引
print(t5.index(3))
# 没有出现的元素会报错 not in tuple
# print(t5.index(588))
print(t5)


