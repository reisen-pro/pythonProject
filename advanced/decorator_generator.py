# 装饰器与生成器练习
import time
from functools import wraps


## 题目1：基础装饰器

# 写一个装饰器 logger(func)：
# - 在函数执行前打印 '开始执行: 函数名'
# - 执行后打印 '执行完成'

def logger(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        print(f'开始执行:{func.__name__}')
        result = func(*args, **kwargs)
        print('执行完成')
        return result

    return wrapper


@logger
def add(a, b):
    return a + b


add(1, 2)


# 输出：
# 开始执行: add
# 执行完成


## 题目2：装饰器带参数

# 写一个装饰器 repeat(n)：
# - 让函数重复执行 n 次

def repeat(n):
    def decorator(func):
        def wrapper(*args, **kwargs):
            for _ in range(n):
                func(*args, **kwargs)

        return wrapper

    return decorator


@repeat(3)
def say():
    print('Hello')


say()  # Hello 打印3次


## 题目3：带参数的函数装饰器

# 写一个装饰器 timeout(seconds)：
# - 如果函数执行超过 n 秒，打印 '超时'
# - 否则打印结果
# 提示：可以用 time 模块

def timeout(seconds):
    def decorator(func):
        def wrapper(*args, **kwargs):
            start_time = time.perf_counter()
            result = func(*args, **kwargs)
            end_time = time.perf_counter()
            use_seconds = (end_time - start_time)
            if use_seconds < seconds:
                return result
            else:
                print('超时')
                return None

        return wrapper

    return decorator


@timeout(2)
def slow():
    time.sleep(0.1)
    return '完成'


slow()


## 题目4：生成器基础

# 写一个生成器 countdown(n)：
# - 从 n 倒数到 0，每次 yield 一个数字

def countdown(n):
    for num in range(n, -1, -1):
        yield num


for i in countdown(5):
    print(i)  # 5 4 3 2 1 0


## 题目5：生成器 + 筛选

# 写一个生成器 fibonacci()：
# - 无限产出斐波那契数列（0, 1, 1, 2, 3, 5, 8, 13...）
# - 用生成器实现

def fibonacci():
    a = 0
    b = 1
    while True:
        a, b = b, a + b
        yield a


# 然后写一个函数 take(gen, n)：
# - 从生成器取前 n 个

def take(gen, n):
    return [next(gen) for _ in range(n)]


fibs = fibonacci()
print(take(fibs, 10))  # [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


## 题目6：yield from

# 写一个生成器 chain(*gens)：
# - 接收多个生成器
# - 用 yield from 把它们串联起来


def chain(*gens):
    for gen in gens:
        yield from gen()

def gen_a():
    yield 1
    yield 2

def gen_b():
    yield 3
    yield 4

for x in chain(gen_a, gen_b):
    print(x)  # 1 2 3 4
