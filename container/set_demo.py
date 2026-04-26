## 题目1：去重

nums = [1, 2, 2, 3, 3, 3, 4, 4, 4, 4]
# 用集合去重，输出不重复的元素
# 期望：{1, 2, 3, 4}
nums = set(nums)
print(nums)

## 题目2：班级统计

class_a = {"张三", "李四", "王五", "赵六"}
class_b = {"李四", "王五", "陈七", "周八"}

# 1. 两个班一共有多少人（去重）
# 2. 同时在两个班的人（交集）
# 3. 只在班级A的人（差集）
# 4. 只在其中一个班的人（对称差）
class_a = set(class_a)
class_b = set(class_b)
print(f"两个班一共:{len(class_a | class_b)}人")
print(f"同时在两个班的人:{class_a & class_b}")
print(f"只在班级A的人:{class_a - class_b}")
print(f"只在其中一个班的人:{class_a ^ class_b}")

## 题目3：找重复

nums = [1, 2, 2, 3, 4, 4, 5]
# 找出列表中出现超过一次的元素
# 期望：{2, 4}
# 提示：用两个集合，一个记录"见过的"，一个记录"重复的"
set1 = set()
set2 = set()
for num in nums:
    if num not in set1:
        set1.add(num)
    else:
        set2.add(num)
print(f"列表中出现超过一次的元素:{set2}")