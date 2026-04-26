# 列表
# 可重复 有序
from operator import index

s = [40, 30, 10, 30, 10, 'Hello', True]
print(type[s])

# 根据下标寻找元素

print(s[0])  # 正向索引从0开始
print(s[-7])  # 反向索引从右到左 从-1 开始

print(s[2])
print(s[-5])

s[6] = False  # 修改

print(s)

# 使用了超出范围的索引
# s[10] = 'test' # IndexError: list assignment index out of range

# 使用del删除指定位置的元素
del s[6]
print(s)

# 遍历
for item in s:
    print(item)

# 切片操作 [开始索引:结束索引:步长]
print(s[0:5:1])  # 读取从0到5的集和 步长为1
print(s[:5:1])  # 省略开始文件
print(s[:5])  # 省略步数

print(s[:5:2])  # 每次步数为2
print(s[:-2:])  # 从头开始,到倒数第二个元素之前（不包含倒数第二个）

# 创建一个成绩管理程序：录入5个学生成绩 → 求平均分/最高/最低 → 排序输出 → 找出不及格
score_arr = []
for i in range(1, 6):
    score = int(input(f"请输入第{i}个学生成绩: "))
    score_arr.append(score)

# Python 内置函数
avg = sum(score_arr) / len(score_arr)
score_max = max(score_arr)
score_min = min(score_arr)

# 排序（从高到低） 从低到高（默认) reverse 就是"反转"
sorted_scores = sorted(score_arr, reverse=True)

# 找不及格
failed = [s for s in score_arr if s < 60]

print(f"平均分: {avg}")
print(f"最高分: {score_max}, 最低分: {score_min}")
print(f"排序后: {sorted_scores}")
print(f"不及格: {failed}")

# 1. 生成 1-10 所有数字的平方列表
# 期望结果: [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
nums = [n * n for n in range(1, 11)]
print(nums)

# 2. 从 1-100 中筛选出所有偶数
# 期望结果: [2, 4, 6, 8, ..., 100]
nums = [n for n in range(1, 101) if n % 2 == 0]
print(nums)

# 3. 把 ["hello", "world", "python"] 全部转成大写
# 期望结果: ['HELLO', 'WORLD', 'PYTHON']
nums = [n.upper() for n in ["hello", "world", "python"]]
print(nums)

# 4. 从 [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 中找出所有能被3整除的数
# 期望结果: [3, 6, 9]
nums = [n for n in range(1, 11) if n % 3 == 0]
print(nums)

nums = [1, 6, 5, 7, 4, 5, 9]
# pop,移除指定索引的元素
nums.pop(5)
# insert,在指定索引处,新增元素
nums.insert(0, 3)
# sort,排序 默认排序 需要倒排,reverse=True
nums.sort(reverse=False)
print(nums)

nums_list1 = [3, 6, 5, 8, 1]
nums_list2 = [6, 9, 4, 3, 2]

# 合并两个列表中的元素
nums_new = []
for e in nums_list1:
    nums_new.append(e)
for f in nums_list2:
    # 合并,去重
    if f not in nums_new:
        nums_new.append(f)
        # 倒序排序
nums_new.sort(reverse=True)

nums_new = []
# 解包* 将列表这一容器解开成为一个一个独立的元素
nums_new = [*nums_list1, *nums_list2]

# 通过+号也可以直接合并
nums_new = nums_list1 + nums_list2
print(nums_new)

# i for i in 序列/列表 前面的i可以运算,也可以加判断

# if在后面,符合条件的数据才进循环
nums_new = [i**2 for i in range(1, 21) if i % 2 == 0]
# if在前面,不影响循环,对循环后的数据进行处理
nums_new = [i**2 if i % 2 == 0 else i for i in range(1, 21) ]
print(nums_new)
