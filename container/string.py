## 切片（Slicing）—— 字符串的"截取"

s = "HelloWorld"

print(f"第一个字符:{s[0]}")  # "H"       第一个字符
print(f"最后一个字符:{s[-1]}")  # "d"       最后一个字符
print(f"从索引2到5（不含5）:{s[2:5]}")  # "llo"     从索引2到5（不含5）
print(f"从索引2到最后:{s[2:]}")  # "lloWorld" 从索引2到最后
print(f"从头到索引5（不含5）:{s[:5]}")  # "Hello"   从头到索引5（不含5）
print(f"步长2，每隔一个取一个:{s[::2]}")  # "Hlool"   步长2，每隔一个取一个
print(f"反转！:{s[::-1]}")  # "dlroWolleH" 反转！

## 索引示意图：
"""
  H   e   l   l   o   W   o   r   l   d
  0   1   2   3   4   5   6   7   8   9
 -10 -9  -8  -7  -6  -5  -4  -3  -2  -1
"""

print("-------------------------------------------")

## 常用方法
s = "  Hello, World!  "

print(f"找位置，找不到返回-1,{s.find("World")}")  # 6  找位置，找不到返回-1
print(f"统计出现次数:{s.count("l")}")  # 3  统计出现次数
print(f"替换:{s.replace("World", "Python")}")  # 替换
print(f"分割:{s.split(",")}")  # ["Hello", "World!"]  分割
print(f"去掉首尾空格:{s.strip()}")  # "Hello, World!"  去掉首尾空格
print(f"大写:{s.upper()}")  # "  HELLO, WORLD!  "
print(f"小写:{s.lower()}")  # "  hello, world!  "
print(f"是否以{s.startswith("Hello")}开头")  # True
print(f"是否已{s.endswith("!")}结束")  # True

## 判断类型
print("abc".isalpha())  # True  是否全是字母
print("123".isdigit())  # True  是否全是数字
print("abc123".isalnum())  # True  是否是字母或数字
print("   ".isspace())  # True  是否全是空格

## 字符串拼接.join()
words = ["Hello", "World", "Python"]
" ".join(words)      # "Hello World Python"
"-".join(words)      # "Hello-World-Python"

