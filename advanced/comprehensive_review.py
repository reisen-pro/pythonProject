# 综合复习测验 - 覆盖 Stage 1-9

import json
import os
from datetime import datetime
from functools import wraps
from json import JSONDecodeError

from functions.scope import total

"""
📝 说明：本测验综合考察各阶段知识点
每道题可能涉及多个阶段的混合运用
"""

## ═══════════════════════════════════════════════════════════════
## 题目1：综合数据处理（Stage 1-4）
## ═══════════════════════════════════════════════════════════════

"""
给定一个学生成绩字典列表，完成以下任务：

students = [
    {'name': 'Alice', 'scores': [85, 90, 78]},
    {'name': 'Bob', 'scores': [70, 65, 80]},
    {'name': 'Carol', 'scores': [92, 88, 95]},
]

要求：
1. 用 lambda + map 计算每个学生的平均分，添加到字典中 'avg' 键
2. 用 filter 筛选出平均分 >= 85 的学生
3. 用 sorted 按平均分降序排列
4. 返回 [(姓名, 平均分)] 格式的列表
"""

students = [
    {'name': 'Alice', 'scores': [85, 90, 78]},
    {'name': 'Bob', 'scores': [70, 65, 80]},
    {'name': 'Carol', 'scores': [92, 88, 95]},
]


def process_students(students):
    # 1. 计算平均分并添加到字典
    # 拿到所有分数,然后计算平均分
    for stu in students:
        avg = float(sum(stu['scores'])) / len(stu['scores'])
        stu['avg'] = round(avg, 2)

    # 2. 筛选平均分 >= 85
    # 你要求筛选平均分 >= 85 ,但是下面预期也输出84.33,所以我改了一下

    students = list(filter(lambda s: float(s['avg']) >= 85, students))

    # 3. 按平均分降序排列
    students.sort(key=lambda s: s['avg'], reverse=True)
    # 4. 返回 [(姓名, 平均分)] 格式
    result = list(zip((stu['name'] for stu in students), (stu['avg'] for stu in students)))
    return result


result = process_students(students)
print(result)
# 预期输出: [('Carol', 91.67), ('Alice', 84.33)]（Bob被筛掉）


## ═══════════════════════════════════════════════════════════════
## 题目2：类设计 + 运算符重载（Stage 5）
## ═══════════════════════════════════════════════════════════════

"""
设计一个 BankAccount 类：

属性：
- owner: 户主名
- balance: 余额（私有属性，用 _balance）
- transactions: 交易记录列表

方法：
- deposit(amount): 存款，记录交易
- withdraw(amount): 取款，余额不足抛出 ValueError
- __add__: 两个账户合并（余额相加，户主用 'A & B'）
- __str__: 返回 '账户(Alice): 1000元'
- @property balance: 只读访问余额

要求：
1. 用 @property 保护余额
2. 每次存取款记录到 transactions（格式: '+500' 或 '-200'）
"""


class BankAccount:
    def __init__(self, owner, balance, transactions=None):
        if transactions is None:
            transactions = []
        self.owner = owner
        self.__balance = balance
        self.__transactions = transactions

    @property
    def balance(self):
        return self.__balance

    @balance.setter
    def balance(self, value):
        self.__balance = value

    @property
    def transactions(self):
        return self.__transactions

    @transactions.setter
    def transactions(self, value):
        self.__transactions = value

    # 存款
    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f'+{amount}')

    # 取款
    def withdraw(self, amount):
        if amount > self.balance:
            raise ValueError("余额不足")
        self.balance -= amount
        self.transactions.append(f'-{amount}')

    # 账户合并
    def __add__(self, other):
        balance = self.balance + other.balance
        owner = self.owner + ' & ' + other.owner
        return BankAccount(owner, balance)

    def __str__(self):
        return f'账户{self.owner}: {self.balance}'


# 测试
bank_accountA = BankAccount('A', 1000)
bank_accountA.deposit(5000)
print(bank_accountA)
bank_accountA.deposit(3000)
print(bank_accountA)
bank_accountA.withdraw(6000)
print(bank_accountA)
bank_accountB = BankAccount('B', 1000)
bank_accountA = bank_accountA + bank_accountB
print(bank_accountA)

## ═══════════════════════════════════════════════════════════════
## 题目3：异常处理 + 文件操作（Stage 6-7）
## ═══════════════════════════════════════════════════════════════

"""
写一个函数 safe_load_json(filename)：
- 读取 JSON 文件
- 文件不存在返回空字典 {}
- JSON 格式错误返回空字典 {}
- 成功返回解析后的数据

再写一个函数 save_with_backup(data, filename)：
- 如果文件已存在，先备份为 filename.bak
- 然后写入新数据
- 使用 try/except/finally 确保文件句柄关闭
"""


def safe_load_json(filename):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)
    except (FileNotFoundError, JSONDecodeError):
        return {}


def save_with_backup(data, filename):
    try:
        if os.path.exists(filename):
            os.rename(filename, filename + '.bak')
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(data, f, ensure_ascii=False, indent=2)
    except Exception as e:
        print(e)


## ═══════════════════════════════════════════════════════════════
## 题目4：装饰器 + 计时（Stage 8-9）
## ═══════════════════════════════════════════════════════════════

"""
写一个装饰器 measure_and_log(func)：
- 测量函数执行时间（毫秒）
- 打印格式: '[函数名] 执行耗时: XX.XXms'
- 把调用记录写入 log.txt（追加模式）
- 日志格式: [时间] 函数名(参数) -> 结果

提示：
- 用 time.perf_counter()
- 用 datetime.now() 获取时间
- functools.wraps 保留原函数信息
"""

import time


def measure_and_log(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter()
        func_result = func(*args, **kwargs)
        end_time = time.perf_counter()
        cost_time = end_time - start_time
        print(f'[{func.__name__}] 执行耗时: {cost_time * 1000:.2f}ms')
        try:
            # [时间] 函数名(参数) -> 结果
            with open('log.txt', 'a', encoding='utf-8') as f:
                now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
                f.write(f'[{now}] {func.__name__}({args}) -> {func_result}\n')
        except Exception as e:
            print(e)
        return func_result

    return wrapper


@measure_and_log
def slow_sum(n):
    total = 0
    for i in range(n):
        total += i
    time.sleep(1)
    return total


slow_sum(1)

## ═══════════════════════════════════════════════════════════════
## 题目5：生成器 + 数据处理（Stage 9）
## ═══════════════════════════════════════════════════════════════

"""
写一个生成器 read_large_file(filename, chunk_size=100)：
- 每次读取 chunk_size 行（不是全部读入内存）
- yield 一个列表，包含这些行的数据
- 用 try/except 处理文件不存在的情况

写一个函数 count_words(gen)：
- 接收上面的生成器
- 统计所有行的总单词数
- 返回总数

提示：生成器 + yield + 文件读取
"""


def read_large_file(filename, chunk_size=100):
    try:
        with open(filename, 'r', encoding='utf-8') as f:
            while True:
                chunk_lines = []
                for i in range(chunk_size):
                    content = f.readline()
                    if content:
                        chunk_lines.append(content)
                    else:
                        break
                if chunk_lines:
                    yield chunk_lines
                else:
                    break
    except FileNotFoundError:
        print('文件不存在')


def count_words(gen):
    total = 0
    for chunk in gen:
        for line in chunk:
            words = line.split()
            # len(words) 每一行的单词数量
            total += len(words)
    return total


gen = read_large_file('text_word.txt', 10)
total_count = count_words(gen)
print(f'总数:{total_count}')
## ═══════════════════════════════════════════════════════════════
## 题目6：综合项目 - 学生管理系统（全阶段）
## ═══════════════════════════════════════════════════════════════

"""
设计一个学生管理系统 StudentManager：

要求：
1. 用类实现
2. 学生数据存储在 students.json
3. 启动时从文件加载，退出时保存到文件
4. 实现以下方法：
   - add_student(name, scores): 添加学生
   - remove_student(name): 删除学生
   - get_top_students(n): 返回平均分前 n 名
   - get_average(): 返回全班平均分

5. 用装饰器给 add_student 添加日志
6. 用异常处理确保文件操作安全
7. 用生成器遍历所有学生

这个题把 Stage 1-9 全串起来了！
"""


class StudentManager:

    def __init__(self, filename):
        # 启动时从文件加载，退出时保存到文件
        self.filename = filename
        self.__students = []
        self._load_from_file()

    def __enter__(self):
        return self

    def _load_from_file(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as f:
                self.__students = json.load(f)
        except (FileNotFoundError, JSONDecodeError):
            self.__students = []

    def save(self):
        try:
            with open(self.filename, 'w', encoding='utf-8') as f:
                json.dump(self.__students, f, ensure_ascii=False, indent=2)
        except Exception as e:
            print(f'保存失败: {e}')

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('退出时保存')
        self.save()
        return False

    def iter_students(self):
        for stu in self.__students:
            yield stu

    @measure_and_log
    def add_student(self, name, scores):
        avg = float(sum(scores)) / len(scores)
        self.__students.append({'name': name, 'scores': scores, 'avg': round(avg, 2)})

    def remove_student(self, name):
        self.__students = [stu for stu in self.__students if stu['name'] != name]

    def get_top_students(self, n):
        self.__students.sort(key=lambda s: s['avg'], reverse=True)
        return self.__students[0:n]

    def get_average(self):
        return sum(stu['avg'] for stu in self.__students) / len(self.__students)


# 测试代码
if __name__ == '__main__':
    with StudentManager('students.json') as sm:

        sm.add_student('Alice', [85, 90, 78])
        sm.add_student('Bob', [70, 65, 80])
        sm.add_student('Carol', [92, 88, 95])
        sm.add_student('DuDi', [63, 84, 77])
        sm.add_student('Fui', [93, 88, 92])
        sm.remove_student('Bob')

        print('Top 2:', sm.get_top_students(2))
        print('班级平均:', sm.get_average())

        for student in sm.iter_students():
            print(student)
