# Python 学习路线规划

> 📅 制定日期：2026-04-19
> 🎯 目标：从零基础到能独立完成项目

---

## 学习阶段总览

| 阶段 | 主题 | 状态 |
|------|------|------|
| Stage 1 | 基础核心（数据类型、变量、运算符） | ✅ 已完成 |
| Stage 2 | 控制流程（条件判断、循环） | ✅ 已完成 |
| Stage 3 | 数据容器（列表、元组、字典、集合、字符串高级） | ✅ 已完成 |
| Stage 4 | 函数（函数定义、参数、返回值、作用域） | ✅ 已完成 |
| Stage 5 | 面向对象（类与对象、继承、多态） | ✅ 已完成 |
| Stage 6 | 异常处理（try/except、raise） | ✅ 已完成 |
| Stage 7 | 文件操作（读写、JSON、CSV） | ✅ 已完成 |
| Stage 8 | 模块与包（import、pip、标准库） | ✅ 已完成 |
| Stage 9 | 装饰器与生成器（高级特性） | ✅ 已完成 |
| Stage 10 | 实战项目（综合运用） | 📅 待学习 |

---

## Stage 1: 基础核心 ✅

**学习文件：** `D:\code\pythonProject\base\hello_data.py`

**知识点：**
- 字面量（整数、浮点数、布尔、字符串、None）
- 变量定义与命名规则
- 类型注解（type hint）
- 变量可重新赋值

**小练习：** ✅ 已完成（变量基础练习）

---

## Stage 2: 控制流程 ✅

**学习文件：** `D:\code\pythonProject\base\loop.py`、`operator_type.py`

**知识点：**
- 算术运算符（+、-、*、/、//、%、**）
- 比较运算符（==、!=、>、<、>=、<=）
- 逻辑运算符（and、or、not）
- 赋值运算符（+=、-=、*=、/=）
- 条件判断（if、elif、else）
- match-case 多分支匹配
- while 循环
- for 循环与 range()
- break 与 continue
- 嵌套循环

**小练习：** ✅ 已完成（猜数字游戏、九九乘法表）

---

## Stage 3: 数据容器 ✅ 已完成

### 3.1 列表（List）✅

**学习文件：** `D:\code\pythonProject\container\list.py`、`list_advanced.py`

**已学知识点：**
- 列表创建与特点（可重复、有序）
- 正向索引与反向索引
- 列表修改
- del 删除元素
- for 循环遍历
- 切片操作 [start:end:step]
- 内置函数 sum() / max() / min() / sorted()
- 列表推导式（转换 + 筛选 + if-else）
- 列表方法 pop() / insert() / sort()
- 列表合并（+ 运算符、* 解包、循环合并去重）
- 二维列表/矩阵（对角线、转置、求和）

**小练习：** ✅ 已完成（成绩管理、推导式4题、矩阵3题、合并去重、筛选平方、正数提取）

---

### 3.2 元组（Tuple）✅

**学习文件：** `D:\code\pythonProject\container\tuple.py`、`tuple_demo.py`

**已学知识点：**
- 元组创建与特点（不可变、有序、可重复）
- 单元素元组（必须加逗号）
- 元组索引与切片
- 元组解包（a, b = b, a 交换变量）
- 函数返回多值

**小练习：** ✅ 已完成（元组解包三道题）

---

### 3.3 字典（Dictionary）✅

**学习文件：** `D:\code\pythonProject\container\dict_demo.py`、`dictionary.py`

**已学知识点：**
- 字典创建 {key: value}
- 字典基本操作（添加/修改/删除/访问）
- get() 方法（避免 KeyError）
- keys() / values() / items()
- 字典嵌套（字典里套字典）
- collections.Counter 计数器
- max() + key 参数找最大值对应的键

**小练习：** ✅ 已完成（个人信息、词频统计、成绩系统）

---

### 3.4 集合（Set）✅

**学习文件：** `D:\code\pythonProject\container\set.py`、`set_demo.py`

**已学知识点：**
- 集合创建与特点（无序、不重复）
- add() / remove() / discard()
- 集合运算：| (并集) & (交集) - (差集) ^ (对称差)
- set() 去重应用
- 两个集合追踪重复元素

**小练习：** ✅ 已完成（去重、班级统计、找重复）

---

### 3.5 字符串高级 ✅

**学习文件：** `D:\code\pythonProject\container\str_advanced.py`

**已学知识点：**
- 字符串切片 [start:end:step]
- 反转字符串 [::-1]
- isupper() / islower() / isdigit() / isalpha()
- upper() / lower() / strip()
- split() / join()
- list.reverse() 返回 None 的坑（原地修改，不返回值）

**小练习：** ✅ 已完成（切片、统计、密码验证、单词反转）

---

## Stage 4: 函数 ✅ 已完成

### 4.1 函数基础 ✅

**学习文件：** `D:\code\pythonProject\functions\func_basic.py`

**已学知识点：**
- 函数定义 def 与调用
- 参数与返回值
- 多返回值（元组解包）
- 内置函数 max() 的灵活使用

**小练习：** ✅ 已完成（打招呼、计算器、找最大值、判断奇偶）

---

### 4.2 函数参数 ✅

**学习文件：** `D:\code\pythonProject\functions\func_param.py`

**已学知识点：**
- 默认参数（exponent=2）
- 多默认参数（age=18, city="未知"）
- 返回 None 的函数（无 return）
- 列表成员判断 `in`
- 三元表达式

**小练习：** ✅ 已完成（power、info、find_and_print）

---

### 4.3 变量作用域 ✅

**学习文件：** `D:\code\pythonProject\functions\scope.py`

**已学知识点：**
- 局部变量 vs 全局变量
- global 关键字
- 函数内修改全局变量
- 可变对象（list/dict）不需要 global
- UnboundLocalError 的原因

---

### 4.4 高级函数特性 ✅

**学习文件：** `D:\code\pythonProject\functions\advanced_func.py`

**已学知识点：**
- 不定长参数 `*args`（元组）和 `**kwargs`（字典）
- 函数作为参数传递（回调函数）
- 匿名函数 `lambda`
- 高阶函数：`map`（映射）、`filter`（筛选）、`reduce`（累积）
- 递归函数（阶乘、斐波那契）

**小练习：** ✅ 已完成（7题，6题直接对，1题踩坑后修复）

---
```

**题目2：Lambda 与高阶函数**
```
1. 用 lambda 和 map 将列表中所有数字平方
2. 用 lambda 和 filter 找出列表中所有偶数
3. 用 lambda 和 sort 对字典列表排序
4. 用 reduce 计算列表所有元素的乘积
```

---

## Stage 5: 面向对象编程（OOP）

### 5.1 类与对象 ✅

**学习文件：** `D:\code\pythonProject\oop\class_basics.py`

**已学知识点：**
- 类定义 `class` 与对象创建
- `__init__` 构造函数
- `self` 参数
- 实例属性 vs 类属性
- 实例方法
- `__str__` 字符串表示
- 链式调用（`return self`）

**小练习：** ✅ 已完成（Person、Calculator链式调用、BankAccount、Counter类属性）

**📁 建议文件：** `D:\code\pythonProject\oop\class_basics.py`

**知识点：**
```
1. 类定义 class
2. __init__ 构造函数
3. self 参数
4. 实例属性 vs 类属性
5. 实例方法 vs 类方法 vs 静态方法
6. __str__ 和 __repr__
```

### 5.2 继承与多态 ✅

**学习文件：** `D:\code\pythonProject\oop\inheritance.py`

**已学知识点：**
- 父类与子类（继承语法）
- `super()` 调用父类方法
- 方法重写（Override）
- 多态（同一方法，不同行为）
- `isinstance()` 类型判断

**小练习：** ✅ 已完成（Vehicle继承、多态show_vehicle、isinstance判断、员工系统）

**📁 建议文件：** `D:\code\pythonProject\oop\inheritance.py`

**知识点：**
```
1. 单继承
2. 多继承（MRO）
3. super() 调用父类
4. 方法重写
5. 多态
6. isinstance() 和 issubclass()
```

### 5.3 面向对象高级

**📁 建议文件：** `D:\code\pythonProject\oop\oop_advanced.py`

**知识点：**
```
1. 封装（私有属性/方法）
2. @property 装饰器
3. __slots__ 限制属性
4. 运算符重载（__add__, __eq__ 等）
5. 描述符
```

**🎮 实战项目：重构贪吃蛇**
```
用面向对象的方式重构贪吃蛇游戏：

classes:
- Game（游戏主类）
- Snake（蛇类）
- Food（食物类）
- ScoreManager（分数管理类）

每个类负责自己的逻辑，体现封装和模块化思想。
```

---

## Stage 6: 异常处理

**📁 建议文件：** `D:\code\pythonProject\base\exception_handling.py`

**知识点：**
```
1. try/except/finally
2. 多个 except
3. except Exception as e
4. raise 主动抛出异常
5. 自定义异常类
6. 常见内置异常（ValueError, TypeError, KeyError, IndexError等）
7. 异常的最佳实践
```

**小题目：**

**题目1：健壮的计算器**
```
写一个计算器，能处理：
1. 除以零
2. 输入非数字
3. 输入运算符不合法
4. 使用 try/except 确保程序不崩溃
```

---

## Stage 7: 文件操作

**📁 建议文件：** `D:\code\pythonProject\base\file_io.py`

**知识点：**
```
1. open() / close()
2. with open() 自动关闭
3. 读取模式 'r' / 写入模式 'w' / 追加模式 'a'
4. read() / readline() / readlines()
5. write() / writelines()
6. JSON文件操作（json.load / json.dump）
7. CSV文件操作（csv模块）
```

**🎮 实战项目：贪吃蛇数据持久化**
```
给贪吃蛇添加数据保存功能：
1. 保存最高分到文件
2. 保存游戏设置到JSON文件
3. 保存排行榜到CSV文件
4. 游戏启动时自动加载设置和历史记录
```

---

## Stage 8: 模块与包

**📁 建议文件：** `D:\code\pythonProject\base\module_demo.py`

**知识点：**
```
1. import 与 from...import
2. 模块的 __name__
3. 自定义模块
4. 包的结构 __init__.py
5. pip 安装第三方库
6. 常用标准库（os, sys, time, datetime, random, collections等）
```

**小题目：**

**题目1：批量文件处理工具**
```
写一个文件处理工具：
1. 列出指定目录下所有文件
2. 统计每个文件的大小
3. 找出最大的文件
4. 按修改时间排序
5. 批量重命名文件
```

---

**学习文件：** `D:\code\pythonProject\advanced\decorator_generator.py`

**知识点：**
```
1. 装饰器基础（@decorator）
2. 带参数的装饰器（repeat(n) 三层嵌套）
3. functools.wraps 保留原函数信息
4. 生成器（yield）
5. yield from 串联生成器
6. 无限生成器（fibonacci）
```

**小练习：** ✅ 已完成（6题，装饰器3题+生成器3题）

---

## Stage 10: 实战综合项目

### 项目1：贪吃蛇（升级版）
**目标：** 完整版贪吃蛇，含所有功能

### 项目2：五子棋 / 俄罗斯方块

### 项目3：命令行 Todo 应用
**目标：** 带文件存储的命令行待办事项管理器

### 项目4：图片批量处理器
**目标：** 使用 PIL 库批量处理图片

---

## 学习进度记录

| 日期 | 完成阶段 | 练习题 | 备注 |
|------|---------|--------|------|
| 2026-04-19 | Stage 1-3.1 | list.py, loop.py | 基础扎实，继续加油！ |
| 2026-04-22 | Stage 3.1 补充 | list.py, list_advanced.py | 自学补充推导式、合并去重、矩阵等知识点 |
| 2026-04-19 | Stage 3.2-3.3 | tuple_demo.py | 元组解包掌握很快 |
| 2026-04-22 | Stage 3.4-3.5 | dict_demo.py, set_demo.py | 字典用得越来越熟练 |
| 2026-04-22 | Stage 3.6 | str_advanced.py | 切片、方法、密码验证全过 |
| 2026-04-22 | Stage 4.1 | func_basic.py | 函数基础完成，继续参数与作用域 |
| 2026-04-23 | Stage 4.2 | func_param.py | 三题全对，默认参数掌握很好 |
| 2026-04-23 | Stage 4.3 | scope.py | 四题全对，作用域理解到位 |
| 2026-04-24 | Stage 4.4 | advanced_func.py | 七题完成，lambda/map/filter/reduce/递归全掌握 |
| 2026-04-24 | Stage 5.1 | class_basics.py | 四题全对，类/对象/链式调用 |
| 2026-04-24 | Stage 5.2 | inheritance.py | 四题全对含选做，继承/多态/重写掌握 |
| 2026-04-25 | Stage 5.3 | oop_advanced.py | 三题完成，封装/@property/运算符重载全掌握 |
| 2026-04-27 | Stage 9 综合复习 | decorator_generator.py, comprehensive_review.py | 6题全对！装饰器+生成器+综合运用全部掌握 |

---

## 资源推荐

**文档：**
- 官方文档：https://docs.python.org/zh-cn/3/
- 菜鸟教程：https://www.runoob.com/python3/python3-tutorial.html

**练习平台：**
- LeetCode（算法）
- 菜鸟教程在线编辑器
- 黑客松（HackerRank）

**书籍推荐：**
- 《Python编程：从入门到实践》
- 《Python核心编程》

---

*Keep learning, keep coding! 🚀*
