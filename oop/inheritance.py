# 继承与多态练习

## 题目1：基础继承

# 定义父类 Vehicle（交通工具）：
# - __init__(self, brand, color)
# - __str__(self)：返回 "XX品牌, XX颜色"

class Vehicle:
    def __init__(self, brand, color):
        self.brand = brand
        self.color = color

    def get_info(self):
        print("这是一辆交通工具")

    def __str__(self):
        return f"{self.brand}牌, {self.color}色"


# 定义子类 Car(Vehicle)：
# - __init__(self, brand, color, seats)
# - 用 super() 调用父类 __init__
# - 新增属性 seats（座位数）

class Car(Vehicle):
    def __init__(self, brand, color, seats):
        super().__init__(brand, color)
        self.seats = seats

    def get_info(self):
        print(f"{self.brand}牌轿车, {self.seats}座")

    def __str__(self):
        return f"{self.brand}牌, {self.color}色,{self.seats}座"


# 定义子类 Bike(Vehicle)：
# - __init__(self, brand, color, has_basket)
# - 用 super() 调用父类 __init__
# - 新增属性 has_basket（有无，布尔值）

class Bike(Vehicle):
    def __init__(self, brand, color, has_basket):
        super().__init__(brand, color)
        self.has_basket = has_basket

    def get_info(self):
        print(f"{self.brand}牌自行车, {'有' if self.has_basket else '无'}车筐")

    def __str__(self):
        return f"{self.brand}牌, {self.color}色,{'有' if self.has_basket else '无'}车筐"


## 题目2：方法重写 + 多态

# 在题目1的基础上：
# Vehicle 添加方法 get_info(self)：返回 "这是一辆交通工具"

# Car 重写 get_info(self)：返回 "XX品牌轿车，XX座"
# Bike 重写 get_info(self)：返回 "XX品牌自行车，有/无车筐"

# 定义函数 show_vehicle(vehicle)：
# 调用 vehicle.get_info() 并打印

# 测试：分别传入 car 和 bike 对象，观察不同输出

def show_vehicle(vehicle):
    vehicle.get_info()


car = Car("奔驰", "黑", 5)
bike = Bike("凤凰", "白", True)
show_vehicle(car)
show_vehicle(bike)

## 题目3：isinstance 判断

# 创建上面定义的 car 和 bike 对象
# 用 isinstance 判断并打印：
# - car 是 Car 的实例吗？
# - car 是 Vehicle 的实例吗？
# - bike 是 Car 的实例吗？
# - bike 是 Vehicle 的实例吗？

print(f"car{'是' if isinstance(car, Car) else '不是'} Car 的实例吗")
print(f"car{'是' if isinstance(car, Vehicle) else '不是'} Vehicle 的实例吗")
print(f"bike{'是' if isinstance(bike, Car) else '不是'} Car 的实例吗")
print(f"bike{'是' if isinstance(bike, Vehicle) else '不是'} Vehicle 的实例吗")


## 题目4：综合挑战 — 员工系统（选做）

# 父类 Employee：
# - __init__(self, name, salary)
# - get_salary(self)：返回 salary
# - __str__(self)：返回 "姓名:XX, 月薪:XX"

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

    def get_salary(self):
        return self.salary

    def __str__(self):
        return f"姓名:{self.name}, 月薪:{self.salary}"

class Manager(Employee):
    def __init__(self, name, salary, bonus):
        super().__init__(name, salary)
        self.bonus = bonus

    def get_salary(self):
        return self.salary + self.bonus

class Programmer(Employee):
    def __init__(self, name, salary, overtime_hours, hourly_rate):
        super().__init__(name, salary)
        self.overtime_hours = overtime_hours
        self.hourly_rate = hourly_rate

    def get_salary(self):
        return self.salary + (self.overtime_hours * self.hourly_rate)


# 创建三个对象，分别打印，观察 get_salary 的不同计算方式
employee = Employee("CC", 2000)
manager = Manager("COCO", 2000, 1000)
programmer = Programmer("COCO", 2000, 10, 50)
print(f"employee.get_salary:{employee.get_salary()}")
print(f"manager.get_salary:{manager.get_salary()}")
print(f"programmer.get_salary:{programmer.get_salary()}")
