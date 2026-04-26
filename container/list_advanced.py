matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
# 题目1：对角线
# 打印主对角线元素（1, 5, 9）
# 提示：主对角线就是 行索引==列索引 的位置
x = 0
y = 0
result = []
for row in matrix:
    for item in row:
        if y == x:
            result.append(matrix[x][y])
            y += 1
            continue
    x += 1
print(result)
# 题目2：转置矩阵

# 行列互换,把上面那个矩阵变成：
# [1, 4, 7]
# [2, 5, 8]
# [3, 6, 9]
# 提示：原来的 matrix[r][c] 变成新矩阵的 [c][r]

x = 0
new_arr = []
for row in matrix:
    add_arr = []
    y = 0
    for item in row:
        add_arr.append(matrix[y][x])
        y += 1
        if y < len(row):
            continue
    x += 1
    new_arr.append(add_arr)
print(new_arr)

# 用while
x = 0
y = 0
new_arr = []
# 几行
while x < len(matrix):
    y = 0
    add_arr = []
    # 一行几个
    while y < len(matrix[x]):
        add_arr.append(matrix[y][x])
        y += 1
    x += 1
    new_arr.append(add_arr)
print(new_arr)

# zip(*matrix) 是 Python 的黑魔法,现在不用深究,以后会学到。
transposed = [list(row) for row in zip(*matrix)]
print(transposed)

# 题目3：矩阵求和
# 计算 matrix 中所有元素的和（1+2+3+4+5+6+7+8+9 = 45）
# 用嵌套循环累加
num_sum = 0
for row in matrix:
    for value in row:
        num_sum += value
print(num_sum)

# 用sum函数 结合前面的 (n for n in )
total = sum(sum(row) for row in matrix)

# 将如下多个列表合并为一个列表,并去重重复元素,排好序（升序）后输出到控制台。
# 合并如下三个列表,并对合并后的列表进行元素的去重,然后排好序后输出到控制台
list1 = ['M', 'A', 'C', 'E', 'F', 'G', 'H', 'L', 'N', 'I', 'J', 'K', 'O']
list2 = ['X', 'Z', 'T', 'Y', 'E', 'F', 'G']
list3 = ['W', 'A', 'S', 'D']
word_list = [*list1, *list2, *list3]
word_list = []
word_list = list1 + list2 + list3
list1.sort()
print(f"排序后的集和:{list1}")

# 将如下列表中能被3或5整除的元素提出来,并获取这些数字对应的平方,组成一个新的列表。
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16
    , 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30]

list1 = [i**2 for i in list1 if i % 3 == 0 or i % 5 == 0]
print(f"被3或5整除的数的平方的集和:{list1}")

# 将如下列表中的正数提取出来,封装为一个新的列表。
list1 = [11, 2, 31, 4, -5, 15, 17, 28, 49, 10, -11, 16, 54, -14, 36, -16, 87, -39]
list1 = [i for i in list1 if i > 0]
print(f"正整数集和:{list1}")
