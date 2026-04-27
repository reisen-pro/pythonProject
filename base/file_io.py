from datetime import datetime

# 文件读写练习

## 题目1：写入并读取

# 写一个函数 write_names(names, filename)：
# - 把列表 names 里的每个名字写入文件，每行一个
# 再写一个函数 read_names(filename)：
# - 读取文件，返回名字列表（去掉换行符）

"""
"r"只读（文件不存在报错）
"w"写入（覆盖，不存在则创建）
"a"追加（不覆盖，不存在则创建）
"rb"二进制读（图片/音频等）
"""


def write_names(names, filename):
    with open(filename, "w", encoding="utf-8") as f:
        for name in names:
            f.write(f"{name}\n")


def read_names(filename):
    with open(filename, "r", encoding="utf-8") as f:
        return [line.strip() for line in f]


# 测试：
write_names(['Alice', 'Bob', 'Charlie'], 'names.txt')
print(read_names('names.txt'))  # ['Alice', 'Bob', 'Charlie']


## 题目2：统计行数和字符数

# 写一个函数 file_stats(filename)：
# - 返回一个字典 {'lines': X, 'chars': X, 'words': X}
# - lines = 总行数
# - chars = 总字符数（不含换行符）
# - words = 总单词数（按空格分割）
def file_stats(filename):
    lines = 0
    chars = 0
    words = 0
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines += 1
            chars += len(line.rstrip('\n'))
            words += len(line.split())

    return {'lines': lines, 'chars': chars, 'words': words}


print(file_stats('names.txt'))


## 题目3：追加日志

# 写一个函数 log_message(message, filename='log.txt')：
# - 把消息追加写入文件
# - 格式：[2026-04-27 09:00:00] 消息内容
# - 用 datetime 模块获取当前时间
#
# 提示：
# from datetime import datetime
# now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#
# 测试：连续调用3次，查看 log.txt 内容


def log_message(message, filename='log.txt'):
    with open(filename, "a", encoding="utf-8") as f:
        now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        f.write(str([now]) + " " + message + "\n")

log_message("hello")
log_message("world")
log_message("!")