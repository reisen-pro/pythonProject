# 面向对象高级特性练习
from urllib.parse import uses_fragment

from container.dictionary import students


## 题目1：封装 + @property

# 定义类 BankAccount：
# - 私有属性 __balance（余额）、__owner（账户名）
# - @property balance：只读，返回余额
# - @property owner：只读，返回账户名
# - deposit(amount)：存款，amount 必须 > 0，否则打印"存款金额必须大于0"
# - withdraw(amount)：取款，amount 必须 > 0 且 <= balance，否则打印对应错误
# - __str__：返回 "账户:XX, 余额:XX"
class BankAccount:
    def __init__(self, owner, balance):
        self.__balance = balance
        self.__owner = owner

    @property
    def balance(self):
        return self.__balance

    @property
    def owner(self):
        return self.__owner

    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
        else:
            print("存款金额必须大于0")

    def withdraw(self, amount):
        if amount > 0:
            if amount <= self.__balance:
                self.__balance -= amount
            else:
                print("余额不足")
        else:
            print("取款金额必须大于0")

    def __str__(self):
        return f"账户:{self.__owner}, 余额:{self.__balance}"


# 测试：
acc = BankAccount("张三", 1000)
# print(acc.balance)   # 1000 无法直接调用私有属性
# print(acc.owner)     # 张三 无法直接调用私有属性
acc.deposit(500)
acc.withdraw(200)
print(acc)  # 账户:张三, 余额:1300
acc.deposit(-100)  # 存款金额必须大于0
acc.withdraw(9999)  # 余额不足


## 题目2：运算符重载


# 定义类 Money（金额）：
class Money:
    def __init__(self, amount, currency="CNY"):
        self.amount = amount
        self.currency = currency

    def __add__(self, money):
        if self.currency == money.currency:
            return Money(self.amount + money.amount, self.currency)
        else:
            print("货币类型不同")
            return None

    def __sub__(self, money):
        if self.currency == money.currency:
            return Money(self.amount - money.amount, self.currency)
        else:
            print("货币类型不同")
            return None

    def __eq__(self, money):
        return self.currency == money.currency and self.amount == money.amount

    def __lt__(self, money):
        if self.currency == money.currency:
            return self.amount < money.amount
        else:
            print("货币类型不同")
            return False

    def __str__(self):
        return f"{self.amount} {self.currency}"


# - __init__(self, amount, currency="CNY")
# - __add__：两个 Money 相加（currency 相同才能加，否则打印"货币类型不同"并返回 None）
# - __sub__：两个 Money 相减（同上）
# - __eq__：判断两个 Money 是否相等（amount 和 currency 都相同）
# - __lt__：判断 self < other（同种货币才比较）
# - __str__：返回 "XX CNY" 或 "XX USD"

# 测试：
m1 = Money(100)
m2 = Money(50)
m3 = Money(30, "USD")
print(m1 + m2)  # 150 CNY
print(m1 - m2)  # 50 CNY
print(m1 == m2)  # False
print(m2 < m1)  # True
print(m1 + m3)  # 货币类型不同


## 题目3：综合挑战 — 学生成绩管理系统（选做）

# 定义类 Student：
# - 私有属性 __name, __scores（成绩列表）
# - @property name：只读
# - @property scores：只读
# - add_score(score)：添加成绩，0-100 之间才合法
# - average：@property，返回平均分（保留1位小数）
# - grade：@property，根据平均分返回等级
#     90+ → A，80+ → B，70+ → C，60+ → D，否则 → F
# - __str__：返回 "XX - 平均分:XX, 等级:X"
# - __lt__：按平均分比较（用于排序）

class Student:

    def __init__(self, name):
        self.__grade = "F"
        self.__average = 0.0
        self.__name = name
        self.__scores = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        self.__name = value

    @property
    def scores(self):
        return self.__scores

    @scores.setter
    def scores(self, value):
        self.__scores = value

    @property
    def average(self):
        return self.__average

    @average.setter
    def average(self, value):
        self.__average = value

    @property
    def grade(self):
        return self.__grade

    @grade.setter
    def grade(self, value):
        self.__grade = value

    def add_score(self, score):
        if 0 <= score <= 100:
            self.__scores.append(score)
            self.get_average()
            self.get_grade()
        else:
            print(f"{score}不合法")

    def get_average(self):
        self.average = sum(self.__scores) / len(self.__scores)

    def get_grade(self):
        average = self.average
        if 90 <= average <= 100:
            grade = "A"
        elif 80 <= average < 90:
            grade = "B"
        elif 70 <= average < 80:
            grade = "C"
        elif 60 <= average < 70:
            grade = "D"
        else:
            grade = "F"
        self.grade = grade

    def __str__(self):
        return f"{self.name} - 平均分:{self.average}, 等级:{self.__grade}"

    def __repr__(self):
        # 直接复用 __str__
        return self.__str__()

    def __lt__(self, student):
        return self.__average < student.__average


# 定义类 Classroom：
# - students 列表
# - add_student(student)：添加学生
# - top_student()：返回平均分最高的学生
# - class_average()：返回全班平均分
# - rank()：返回按平均分排序的学生列表（从高到低）

class Classroom:
    def __init__(self, student_list=None):
        if student_list is None:
            student_list = []
        self.__students = student_list

    def add_student(self, student):
        self.__students.append(student)

    def top_student(self):
        return max(self.__students, key=lambda x: x.average)

    def class_average(self):
        return sum(student.average for student in self.__students) / len(self.__students)

    def rank(self):
        return sorted(self.__students, reverse=True)


# 测试：
s1 = Student("张三")
s1.add_score(80)
s1.add_score(80)
s1.add_score(80)
print(s1)  # 张三 - 平均分:85.0, 等级:B

s2 = Student("李四")
s2.add_score(90)
s2.add_score(90)
s2.add_score(90)
print(s2)

s3 = Student("王五")
s3.add_score(65)
s3.add_score(65)
s3.add_score(65)
print(s3)

c1 = Classroom()
c1.add_student(s1)
c1.add_student(s2)
c1.add_student(s3)
print(f"均分最高的学生:{c1.top_student()}")
print(f"班级平均分:{c1.class_average()}")
print(c1.rank())
