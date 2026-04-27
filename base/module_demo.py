# 模块与包练习

import os
import sys
import time
from datetime import datetime
import random
from collections import Counter


## 题目1：os 模块

# 写一个函数 list_files(dir_path)：
# - 列出目录下所有文件（不包括文件夹）
# - 返回文件路径列表
# 提示：os.listdir() 或 os.walk()

def list_files(dir_path):
    file_list = os.listdir(dir_path)
    return [f for f in file_list if os.path.isfile(os.path.join(dir_path, f))], [f for f in file_list if os.path.isdir(os.path.join(dir_path, f))]


files, dirs = list_files("../")
print(f"目录下所有文件（不包括文件夹）:{files}")
print(f"文件路径列表:{dirs}")


# 测试当前目录的文件
# 我测试了项目根目录,它下面既有文件,也有文件夹

## 题目2：time 模块

# 写一个函数 measure_time(func)：
# - 装饰器形式，测量函数执行时间
# - 返回 (结果, 耗时毫秒)
# 提示：time.time() 或 time.perf_counter()

def measure_time(func):
    # 返回执行的时间的话
    # 结束时间 减去 开始时间
    def wrapper(*args, **kwargs):
        # 开始时间
        start_time = time.perf_counter()
        result = func(*args, **kwargs)
        end_time = time.perf_counter()
        elapsed_ms = (end_time - start_time) * 1000
        return result, f'耗时: {elapsed_ms :.2f}ms'

    return wrapper


# 测试：
@measure_time
def slow():
    time.sleep(0.1)
    return 42


print(slow())  # (42, ~100)


## 题目3：datetime 模块

# 写一个函数 format_time(dt=None)：
# - 参数 dt 是 datetime 对象，默认当前时间
# - 返回格式：'2026-04-27 10:00:00'

def format_time(dt=None):
    if dt is None:
        dt = datetime.now()
    return dt.strftime('%Y-%m-%d %H:%M:%S')


# 再写一个函数 days_between(date1, date2)：
# - 返回两个日期之间的天数

def days_between(date1, date2):
    # 先把字符串转换成时间
    d1 = datetime.strptime(date1, '%Y-%m-%d')
    d2 = datetime.strptime(date2, '%Y-%m-%d')
    # 然后两个时间相减,转换成天
    delta = abs((d2 - d1).days)
    return delta


# 测试：
print(format_time())  # 当前时间
print(days_between('2026-01-01', '2026-04-27'))  # ~116


## 题目4：random 模块

# 写一个函数 shuffle_list(lst)：
# - 随机打乱列表顺序（原地打乱）
# 提示：random.shuffle()

def shuffle_list(lst):
    random.shuffle(lst)


num_lst = [1, 2, 3, 4, 5, 6]
shuffle_list(num_lst)
print(num_lst)


# 再写一个函数 random_choice(lst, n=1)：
# - 从列表随机选 n 个元素（可重复）
# 提示：random.choices()，返回列表

def random_choice(lst, n=1):
    return random.choices(lst, k=n)
print(random_choice(num_lst))

## 题目5：collections.Counter

# 写一个函数 most_common_words(text, n=3)：
# - 返回最常见的 n 个词及出现次数
# - 提示：text.split() 分词，Counter 统计

def most_common_words(text,n=3):
    c = Counter(text.split())
    return c.most_common(n)

# 测试：
text = 'apple banana apple orange banana apple'
print(most_common_words(text, 2))
# # [('apple', 3), ('banana', 2)]