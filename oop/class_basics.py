# 类与对象练习

## 题目1：定义一个简单的类

# 定义类 Person，包含：
# - __init__(self, name, age, city)
# - intro(self)：打印 "我叫XX，今年XX岁，来自XX"
# - __str__(self)：返回 "姓名:XX, 年龄:XX, 城市:XX"

class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def intro(self):
        print(f"你好，我是{self.name}，{self.age}岁，来自{self.city}")

    def __str__(self):
        return f"姓名:{self.name}, 年龄:{self.age}, 城市:{self.city}"


p1 = Person("张三", 20, "北京")
p1.intro()  # 期望输出: 我叫张三，今年20岁，来自北京
print(p1)  # 期望输出: 姓名:张三, 年龄:20, 城市:北京


## 题目2：计算器类

# 定义类 Calculator，包含：
# - __init__(self)：result = 0
# - add(self, n)：result += n，返回 self（方便链式调用）
# - subtract(self, n)：result -= n，返回 self
# - multiply(self, n)：result *= n，返回 self
# - divide(self, n)：result /= n，返回 self
# - get_result(self)：返回当前结果

class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, n):
        self.result += n
        return self

    def subtract(self, n):
        self.result -= n
        return self

    def multiply(self, n):
        self.result *= n
        return self

    def divide(self, n):
        self.result /= n
        return self

    def get_result(self):
        return self.result


calc = Calculator()
r = calc.add(10).subtract(3).multiply(2).divide(7).get_result()
print(r)  # 期望: 2.0


# 计算过程: ((0+10-3)*2)/7 = 2.0


## 题目3：银行账户类

# 定义类 BankAccount，包含：
# - __init__(self, owner, balance=0)
# - deposit(self, amount)：存钱，balance += amount
# - withdraw(self, amount)：取钱，
#     如果 balance >= amount 才扣钱，否则打印"余额不足"
# - get_balance(self)：返回当前余额
# - __str__(self)：返回 "账户:XX, 余额:XX"

class BankAccount:
    def __init__(self, owner, balance=0):
        self.owner = owner
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if self.balance < amount:
            print("余额不足")
        else:
            self.balance -= amount

    def get_balance(self):
        return self.balance

    def __str__(self):
        return f"账户:{self.owner},余额:{self.balance}"


account = BankAccount("张三", 1000)
account.deposit(500)
account.withdraw(200)
print(account)  # 期望: 账户:张三, 余额:1300
account.withdraw(2000)  # 期望输出: 余额不足


## 题目4：计数器类（类属性）

# 定义类 Counter，包含：
# - count = 0（类属性，所有对象共享）
# - __init__(self, name)
# - 每次创建新对象时，count += 1
# - __str__(self)：返回 "XX当前计数:XX"

class Counter:
    count = 0

    def __init__(self, name):
        self.name = name
        Counter.count += 1

    def __str__(self):
        return f"{self.name}当前计数:{Counter.count}"



c1 = Counter("A")
c2 = Counter("B")
c3 = Counter("C")
print(c1)  # 期望: A当前计数:3
print(c2)  # 期望: B当前计数:3
print(c3)  # 期望: C当前计数:3
