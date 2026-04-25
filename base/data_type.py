# type() 函数可以显示数据的类型

num_int = 100
print(type(num_int))  # <class 'int'>
print(type("hello"))  # <class 'str'>
print(type(3.14))  # <class 'float'>
print(type(True))  # <class 'bool'>
print(type(None))  # <class 'NoneType'>

# isinstance(data, data_type) 用于判断数据类型
# 参数1: 要判断的数据
# 参数2: 目标数据类型
# 返回值: 布尔值(True/False)
num = 5.0
print(num)  # 5.0
print(isinstance(num, int))  # False (5.0是float类型,不是int)
print(isinstance(num, float))  # True

# .1f float 保留一位小数
print(f"{3.33333:.1f}")
