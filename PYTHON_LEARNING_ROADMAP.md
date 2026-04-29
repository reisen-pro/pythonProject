# Python 学习路线规划

> 📅 制定日期：2026-04-19
> 🎯 目标：**Python 基础 → AI / 机器学习 → 找到 AI 相关工作**

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
| Stage 10 | AI 方向实战项目（简历项目） | 📅 待学习 |
| Stage 11 | 机器学习基础（Scikit-learn） | 📅 待学习 |
| Stage 12 | 深度学习（PyTorch） | 📅 待学习 |
| Stage 13 | LLM / AI Agent（大语言模型应用） | 📅 待学习 |

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

### 3.2 元组（Tuple）✅

**学习文件：** `D:\code\pythonProject\container\tuple.py`、`tuple_demo.py`

**已学知识点：**
- 元组创建与特点（不可变、有序、可重复）
- 单元素元组（必须加逗号）
- 元组索引与切片
- 元组解包（a, b = b, a 交换变量）
- 函数返回多值

**小练习：** ✅ 已完成（元组解包三道题）

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

### 3.4 集合（Set）✅

**学习文件：** `D:\code\pythonProject\container\set.py`、`set_demo.py`

**已学知识点：**
- 集合创建与特点（无序、不重复）
- add() / remove() / discard()
- 集合运算：| (并集) & (交集) - (差集) ^ (对称差)
- set() 去重应用
- 两个集合追踪重复元素

**小练习：** ✅ 已完成（去重、班级统计、找重复）

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

### 4.2 函数参数 ✅

**学习文件：** `D:\code\pythonProject\functions\func_param.py`

**已学知识点：**
- 默认参数（exponent=2）
- 多默认参数（age=18, city="未知"）
- 返回 None 的函数（无 return）
- 列表成员判断 `in`
- 三元表达式

**小练习：** ✅ 已完成（power、info、find_and_print）

### 4.3 变量作用域 ✅

**学习文件：** `D:\code\pythonProject\functions\scope.py`

**已学知识点：**
- 局部变量 vs 全局变量
- global 关键字
- 函数内修改全局变量
- 可变对象（list/dict）不需要 global
- UnboundLocalError 的原因

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

## Stage 5: 面向对象编程（OOP）✅ 已完成

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

### 5.2 继承与多态 ✅

**学习文件：** `D:\code\pythonProject\oop\inheritance.py`

**已学知识点：**
- 父类与子类（继承语法）
- `super()` 调用父类方法
- 方法重写（Override）
- 多态（同一方法，不同行为）
- `isinstance()` 类型判断

**小练习：** ✅ 已完成（Vehicle继承、多态show_vehicle、isinstance判断、员工系统）

### 5.3 面向对象高级 ✅

**学习文件：** `D:\code\pythonProject\oop\oop_advanced.py`

**已学知识点：**
- 封装（私有属性/方法）
- `@property` 装饰器
- 运算符重载（`__add__`、`__str__` 等）
- 类属性 vs 实例属性
- 综合运用：BankAccount + Money + StudentManager

**小练习：** ✅ 已完成（BankAccount封装修正、Money运算符重载、StudentManager上下文管理器）

---

## Stage 6: 异常处理 ✅ 已完成

**学习文件：** `D:\code\pythonProject\base\exception_handling.py`

**已学知识点：**
- try / except / finally
- 多个 except 与 Exception 捕获
- raise 主动抛出
- 自定义异常类
- 安全设计（safe_divide、read_file_safe）

**小练习：** ✅ 已完成（四题全对）

---

## Stage 7: 文件操作 ✅ 已完成

**学习文件：** `D:\code\pythonProject\base\file_io.py`

**已学知识点：**
- 文件读写（with open / read / write）
- write_names / read_names / file_stats / log_message

**小练习：** ✅ 已完成（三题全对）

---

## Stage 8: 模块与包 ✅ 已完成

**学习文件：** `D:\code\pythonProject\base\module_demo.py`

**已学知识点：**
- os / time / datetime / random / collections.Counter
- `__name__ == '__main__'` 入口模式
- pip 安装第三方库

**小练习：** ✅ 已完成（五题全对）

---

## Stage 9: 装饰器与生成器 ✅ 已完成

**学习文件：** `D:\code\pythonProject\advanced\decorator_generator.py`

**已学知识点：**
- 装饰器基础（@decorator、@wraps）
- 带参数装饰器（repeat(n)、timeout(seconds)）
- functools.wraps 保留原函数信息
- 生成器（yield、yield from）
- 无限生成器（fibonacci）

**小练习：** ✅ 已完成（6题，装饰器3题+生成器3题）

**综合复习：** `D:\code\pythonProject\advanced\comprehensive_review.py` ✅ 已完成（6题全对）

---

## ⭐ Stage 10: AI 方向实战项目（简历项目）📅 待学习

**目标：** 完成 1-2 个能写进简历的项目，证明 AI 实战能力

### 项目1：数据分析 + 可视化项目 📊
**数据集：**  Titanic 生存预测 / 电影评分 / 房价预测（Kaggle 公开数据集）
**技术栈：** Pandas + NumPy + Matplotlib + Scikit-learn
**内容：**
1. 数据加载与清洗（缺失值、异常值）
2. 探索性数据分析（EDA）+ 可视化
3. 特征工程（编码、归一化）
4. 训练模型（线性回归 / 逻辑回归 / 随机森林）
5. 模型评估（准确率 / 召回率 / F1）

**面试价值：** ⭐⭐⭐⭐⭐ 数据分析是 AI 岗位面试必考

---

### 项目2：图片分类器（PyTorch）🖼️
**数据集：** CIFAR-10 / MNIST（手写数字）
**技术栈：** PyTorch + NumPy
**内容：**
1. 数据加载（Dataset / DataLoader）
2. 构建神经网络（CNN）
3. 训练循环（forward / backward / optimizer）
4. 模型评估与保存

**面试价值：** ⭐⭐⭐⭐⭐ 证明深度学习落地能力

---

### 项目3：LLM 应用 / AI Agent 🤖
**技术栈：** OpenAI API / LangChain / RAG
**内容：**
1. 调用 LLM API 实现对话
2. 构建 RAG（检索增强生成）系统
3. 实现 AI Agent（工具调用 + 记忆）

**面试价值：** ⭐⭐⭐⭐⭐ 当前最热门方向

---

## Stage 11: 机器学习基础（Scikit-learn）📅 待学习

**📁 建议文件：** `D:\code\pythonProject\ml\scikit_learn_basics.py`

**知识点：**
```
1. NumPy 基础（向量、矩阵运算）
2. Pandas 数据处理
3. Scikit-learn 使用流程（fit / predict / transform）
4. 监督学习：线性回归、逻辑回归、决策树、随机森林
5. 模型评估：train_test_split、cross_val_score
6. 特征工程：标准化、编码、缺失值处理
```

**关键概念（面试重点）：**
- 过拟合 vs 欠拟合
- 偏差 vs 方差
- 交叉验证
- 混淆矩阵（Precision / Recall / F1）

---

## Stage 12: 深度学习（PyTorch）📅 待学习

**📁 建议文件：** `D:\code\pythonProject\dl\pytorch_basics.py`

**知识点：**
```
1. PyTorch 张量（Tensor）操作
2. Dataset / DataLoader
3. 构建神经网络（nn.Module）
4. 损失函数与优化器
5. CNN（卷积神经网络）
6. RNN / LSTM（序列模型）
7. 模型保存与加载
```

**关键概念（面试重点）：**
- 反向传播（Backpropagation）
- 梯度下降与学习率
- Dropout / BatchNorm
- Transformer / Attention 机制

---

## Stage 13: LLM / AI Agent（大语言模型应用）📅 待学习

**知识点：**
```
1. LLM API 调用（OpenAI / Claude / 本地模型）
2. Prompt Engineering（提示词工程）
3. LangChain 框架
4. RAG（检索增强生成）
5. AI Agent（工具调用、记忆、规划）
6. 向量数据库（Chroma / FAISS）
```

**关键概念（面试重点）：**
- Fine-tuning vs RAG vs Prompt Engineering
- Token 与上下文窗口
- Function Calling / Tool Use
- Agent ReAct 模式

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
| 2026-04-27 | Stage 6-7 | exception_handling.py, file_io.py | 异常处理+文件读写四题全对 |
| 2026-04-27 | Stage 7-8 | json_csv.py, module_demo.py | JSON/CSV + 模块练习九题全对 |
| 2026-04-27 | Stage 9 | decorator_generator.py | 装饰器+生成器六题全对 |
| 2026-04-27 | 综合复习 | comprehensive_review.py | Stage 1-9 综合测验六题全对 |

---

## 资源推荐

**文档：**
- 官方文档：https://docs.python.org/zh-cn/3/
- 菜鸟教程：https://www.runoob.com/python3/python3-tutorial.html

**AI/ML 学习资源：**
- 吴恩达 Machine Learning（Coursera）— 机器学习入门必学
- 李沐《动手学深度学习》— PyTorch 实战好书
- Kaggle — 数据集 + 比赛，面试时很有说服力
- Hugging Face — LLM / NLP 最全资源站

**练习平台：**
- LeetCode（刷算法题）
- 菜鸟教程在线编辑器
- Kaggle（数据分析 + 机器学习）

**书籍推荐：**
- 《Python编程：从入门到实践》
- 《机器学习实战》— sklearn 入门经典
- 《深度学习入门：基于 Python 的理论与实现》

---

*Keep learning, keep coding! 🚀*