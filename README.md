# 🐍 Python Learning Journey

> 从零开始的 Python 系统学习记录，包含完整路线图与分阶段练习代码。

---

## 📊 学习进度

| 阶段 | 主题 | 状态 |
|------|------|------|
| Stage 1 | 基础核心（数据类型、变量、运算符） | ✅ 已完成 |
| Stage 2 | 控制流程（条件判断、循环） | ✅ 已完成 |
| Stage 3 | 数据容器（列表、元组、字典、集合、字符串） | ✅ 已完成 |
| Stage 4 | 函数（定义、参数、作用域、高阶函数） | ✅ 已完成 |
| Stage 5 | 面向对象（类、继承、封装、多态） | ✅ 已完成 |
| Stage 6 | 异常处理（try/except、raise） | ✅ 已完成 |
| Stage 7 | 文件操作（读写、JSON、CSV） | ✅ 已完成 |
| Stage 8 | 模块与包（import、pip、标准库） | ✅ 已完成 |
| Stage 9 | 装饰器与生成器 | ✅ 已完成 |
| Stage 10 | 实战项目 | 📅 待学习 |

---

## 📁 项目结构

```
pythonProject/
├── base/               # Stage 1-2 & 6-7：基础语法、控制流程、异常、文件操作
│   ├── hello_data.py
│   ├── data_type.py
│   ├── operator_type.py
│   ├── loop.py
│   ├── exception_handling.py      # 异常处理
│   ├── file_io.py                # 文件读写
│   ├── json_csv.py               # JSON/CSV 操作
│   └── module_demo.py            # 模块练习（os/time/random/Counter）
├── container/          # Stage 3：数据容器
│   ├── list.py
│   ├── list_advanced.py
│   ├── tuple.py
│   ├── dict_demo.py
│   ├── set.py
│   └── str_advanced.py
├── functions/          # Stage 4：函数
│   ├── func_basic.py
│   ├── func_param.py
│   ├── scope.py
│   └── advanced_func.py
├── oop/                # Stage 5：面向对象
│   ├── class_basics.py
│   ├── inheritance.py
│   └── oop_advanced.py
├── advanced/           # Stage 9：高级特性
│   ├── decorator_generator.py    # 装饰器 + 生成器
│   └── comprehensive_review.py    # 综合复习测验（串 Stage 1-9）
├── README.md
└── PYTHON_LEARNING_ROADMAP.md
```

---

## 🧠 已掌握知识点

<details>
<summary><b>Stage 1-2：基础语法</b></summary>

- 变量、数据类型（int / float / str / bool / None）
- 运算符（算术、比较、逻辑、赋值）
- 条件判断（if / elif / else）
- 循环（for / while / break / continue）

</details>

<details>
<summary><b>Stage 3：数据容器</b></summary>

- 列表（增删改查、推导式、二维列表）
- 元组（解包、多返回值）
- 字典（增删改查、遍历、嵌套、Counter）
- 集合（去重、交并差）
- 字符串高级（格式化、切片、常用方法）

</details>

<details>
<summary><b>Stage 4：函数</b></summary>

- 函数定义与调用、默认参数、多返回值
- 变量作用域（局部 / 全局 / global 关键字）
- *args / **kwargs
- lambda、map / filter / reduce
- 递归（阶乘、斐波那契）

</details>

<details>
<summary><b>Stage 5：面向对象</b></summary>

- 类与对象、`__init__`、self
- 实例属性 vs 类属性
- 继承、方法重写、`super()`
- 多态
- 封装、`@property`
- 运算符重载（`__add__`、`__str__` 等）

</details>

<details>
<summary><b>Stage 6：异常处理</b></summary>

- try / except / finally
- 多个 except 与 Exception 捕获
- raise 主动抛出
- 自定义异常类
- 安全设计（safe_divide、read_file_safe）

</details>

<details>
<summary><b>Stage 7-8：文件操作与模块</b></summary>

- 文件读写（with open / read / write）
- JSON（json.load / json.dump）
- CSV（csv.DictReader / csv.DictWriter）
- os / time / datetime / random / collections.Counter
- `__name__ == '__main__'` 入口模式

</details>

<details>
<summary><b>Stage 9：装饰器与生成器</b></summary>

- 装饰器基础（@decorator、@wraps）
- 带参数装饰器（repeat(n)、timeout(seconds)）
- 生成器（yield、yield from）
- 无限生成器（fibonacci）
- 综合运用（@property + 运算符重载 + 装饰器计时日志）

</details>

---

## 🚀 快速开始

```bash
# 克隆项目
git clone https://github.com/reisen-pro/pythonProject.git

# 进入目录
cd pythonProject

# 运行任意练习文件
python base/hello_data.py
python oop/oop_advanced.py
python advanced/comprehensive_review.py
```

> 环境要求：Python 3.10+，无需额外依赖

---

## 📖 学习路线图

详见 [PYTHON_LEARNING_ROADMAP.md](./PYTHON_LEARNING_ROADMAP.md)

---

*持续更新中... 一边踩坑一边成长 🌱*