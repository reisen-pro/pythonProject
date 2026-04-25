## 题目1：切片练习

s = "Python是最有意思的语言！"
# 1. 取前6个字符
# 2. 取最后3个字符
# 3. 反转字符串
# 4. 取"最有意思"四个字
print(f"取前6个字符:{s[:6]}")
print(f"取最后3个字符:{s[-3:]}")
print(f"反转字符串:{s[::-1]}")
print(f"取\"最有意思\"四个字:{s[7:11]}")

## 题目2：统计字母
text = "Hello, Python! Hello, World!"
# 统计大写字母数量
# 统计小写字母数量
# 统计数字数量
# 全部转为大写并打印
big_word_count = 0
litter_word_count = 0
num_count = 0
for word in text:
    if word.isupper():
        big_word_count += 1
    elif word.islower():
        litter_word_count += 1
    elif word.isdigit():
        num_count += 1
print(f"统计大写字母数量:{big_word_count}")
print(f"统计小写字母数量:{litter_word_count}")
print(f"统计数字数量:{num_count}")
print(f"全部转为大写并打印:{text.upper()}")

## 题目3：密码验证
# 让用户输入一个密码，打印是否符合要求
# 1. 长度至少8位
# 2. 包含数字
# 3. 包含字母
# 如果不满足，说明哪条不满足
while True:
    password = input("请输入密码:")
    context_num = False
    context_word = False
    if len(password) < 8:
        print("长度至少8位")
        continue
    for e in password:
        if e.isdigit():
            context_num = True
        if e.isalpha():
            context_word = True
    if not context_num:
        print("不包含数字")
        continue
    if not context_word:
        print("不包含字母")
        continue
    print(f"{password}:符合要求")
    break
## 题目4：单词反转
sentence = "Hello World Python"
# 输出："Python World Hello"
# 提示：split() → reverse → join()

## 可以直接反转
# sentence = sentence.split(" ")[::-1]

## 这里有个小坑,当时
# sentence = sentence.sentence.split(" ")
# sentence = sentence.reverse(self) (反转自己)
# 输出出来是None
# 查了一下,python里,几乎都只对原先的数据做处理,不产生返回值
# 如果要用reverse(),那就得创建一个新容器去接收分割后的列表
sentence_list = sentence.split(" ")
sentence_list.reverse()

print(sentence)

# 回文数判断
str_txt = "黄山落叶松叶落山黄"
print(f"{str_txt} 是否回文 : {str_txt == str_txt[::-1]}")