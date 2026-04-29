"""
NumPy 基础练习
==============
NumPy = Numerical Python，是 AI 领域的数值计算底层库。

核心概念：NumPy 的 ndarray（多维数组）vs Python 原生 list
"""

# ============================================================
# 第1题：NumPy 数组的创建（对比 Python list）
# ============================================================

import numpy as np

# Python 原生列表
python_list = [1, 2, 3, 4, 5]

# NumPy 数组（一维）
arr = np.array([1, 2, 3, 4, 5])

print("Python list:", python_list)
print("NumPy array:", arr)
print("NumPy array 类型:", type(arr))

# 运行后观察：
# - 两者打印出来差不多，但背后的数据结构完全不同
# - list 可以存任意类型，array 只能存同一种类型（更高效）


# ============================================================
# 第2题：NumPy 数组的基本属性
# ============================================================

arr = np.array([1, 2, 3, 4, 5])

print("\n--- 数组属性 ---")
print("shape（形状）:", arr.shape)      # (5,) 表示有5个元素的一维数组
print("dtype（数据类型）:", arr.dtype)  # int64 / int32 等
print("ndim（维度数）:", arr.ndim)     # 1（维度的数量）
print("size（元素总数）:", arr.size)    # 5
print("itemsize（每个元素字节）:", arr.itemsize)  # 8

# 理解 shape：
# [1, 2, 3]       → shape: (3,)    一维数组，3个元素
# [[1,2],[3,4]]   → shape: (2, 2)  二维数组，2行2列
# [[[1],[2]],[[3],[4]]]     → shape: (2, 2, 1) 三维数组


# ============================================================
# 第3题：创建数组的多种方式
# ============================================================

print("\n--- 创建数组的方式 ---")

# 方式1：np.array() — 从 Python 列表转换
arr1 = np.array([0, 1, 2, 3, 4])
print("np.array([0,1,2,3,4]):", arr1)

# 方式2：np.arange() — 类似于 range()
arr2 = np.arange(0, 10, 2)  # 起始0，结束10，步长2
print("np.arange(0,10,2):", arr2)  # [0 2 4 6 8]

# 方式3：np.linspace() — 等差数列（包含终点）
arr3 = np.linspace(0, 1, 5)  # 从0到1，平均分成5个数
print("np.linspace(0,1,5):", arr3)  # [0.   0.25 0.5  0.75 1.  ]

# 方式4：np.zeros() / np.ones() — 全0/全1数组
arr4 = np.zeros(5)
arr5 = np.ones((3, 3))  # 3行3列的二维数组
print("np.zeros(5):", arr4)
print("np.ones((3,3)):\n", arr5)  # \n 换行显示

# 方式5：np.random.rand() — 随机数（0-1之间）
arr6 = np.random.rand(5)
print("np.random.rand(5):", arr6)


# ============================================================
# 第4题：NumPy 的核心优势 — 不用 for 循环！
# ============================================================
# 这就是"向量化"（Vectorization）— 对整个数组同时运算

arr = np.array([1, 2, 3, 4, 5])

# 普通做法（Java 思维）：for 循环
result_for = []
for x in arr:
    result_for.append(x * 2)
print("\nfor循环 *2:", result_for)

# NumPy 做法（向量化）：直接操作整个数组
result_np = arr * 2
print("NumPy *2:    ", result_np)

# 更多例子
print("arr + 10:", arr + 10)      # 每个元素+10
print("arr ** 2:", arr ** 2)      # 每个元素平方
print("arr > 2: ", arr > 2)       # 每个元素判断，返回布尔数组
print("np.sqrt(arr):", np.sqrt(arr))  # 每个元素开根号

# 理解：NumPy 里，arr * 2 不是"数组乘以2"，
# 而是"数组里每个元素都乘以2"。这叫"元素级运算"。


# ============================================================
# 第5题：二维数组（矩阵）
# ============================================================

# 创建 2行3列 的二维数组
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])

print("\n--- 二维数组 ---")
print("matrix:\n", matrix)
print("shape:", matrix.shape)  # (2, 3) — 2行3列
print("ndim:", matrix.ndim)   # 2

# 访问元素：matrix[行, 列]（从0开始）
print("matrix[0, 0]:", matrix[0, 0])  # 第1行第1列 = 1
print("matrix[1, 2]:", matrix[1, 2])  # 第2行第3列 = 6

# 切片：取某一行
print("第1行:", matrix[0, :])      # 所有列
print("第1列:", matrix[:, 0])      # 所有行

# 取子矩阵（2-3行，1-2列）
print("子矩阵:\n", matrix[0:2, 0:2])


# ============================================================
# 第6题：NumPy 常用统计函数
# ============================================================

arr = np.array([1, 2, 3, 4, 5])

print("\n--- 统计函数 ---")
print("sum():   ", arr.sum())    # 总和
print("mean():  ", arr.mean())   # 平均值
print("std():   ", arr.std())    # 标准差（衡量数据分散程度）
print("min():   ", arr.min())    # 最小值
print("max():   ", arr.max())    # 最大值

# 二维数组的统计（可以按行/按列）
matrix = np.array([
    [1, 2, 3],
    [4, 5, 6]
])
print("\n二维数组按列求和（axis=0）:", matrix.sum(axis=0))  # [5 7 9]
print("二维数组按行求和（axis=1）:", matrix.sum(axis=1))  # [ 6 15]


# ============================================================
# 思考题（不写代码，自己想想）
# ============================================================
"""
1. np.array([1, 2, 3]) 和 np.array([[1, 2, 3]]) 的 shape 分别是什么？
   两者有什么区别？（hint: 一个是向量，一个是只有1行的矩阵）
前者是一个一维数组
后者是一个二维数组
两者维度不一样   

2. 如果一个数组 a 的 shape 是 (4, 3)，它代表什么意思？
   这个数组里一共有多少个元素？
这里一共4*3 12个元素,代表这是一个二维数组,四行三列

3. arr = np.arange(1, 10)，不使用循环，怎么得到 [2, 4, 6, 8, 10, 12, 14, 16, 18]？
通过 arr * 2 使每个元素都乘2

4. 为什么 NumPy 比 Python list 快？（hint: 同质性、连续内存、SIMD指令）
这个numpy是整个去处理数据,不需像python list 迭代循环的去处理
python list可以存储不同类型的数据,numpy要求相同类型的数据,这就方便了numpy省去了对类型的检查
python list存储的是对象,numpy存储的是数值,更快
连续内存：NumPy 的数组在内存中是连续存放的，就像一排紧挨着的抽屉，
CPU 一次读取一大块；Python list 的每个元素是独立对象，分散在内存各处，读取慢。
SIMD 指令：CPU 可以用一条指令同时处理多个数据（类似一次开多个抽屉），
NumPy 能利用这个，Python for 循环只能一条一条处理。

"""

import time
# 创建大数据集
size = 1000000
python_list = list(range(size))
numpy_arr = np.arange(size)

# Python list 求和
start = time.time()
sum_list = sum(python_list)
time_list = time.time() - start
print(f"Python list 耗时: {time_list:.4f}秒")

# NumPy 求和
start = time.time()
sum_numpy = numpy_arr.sum()
time_numpy = time.time() - start
print(f"NumPy 耗时: {time_numpy:.4f}秒")

print(f"NumPy 快了 {time_list/time_numpy:.1f} 倍")