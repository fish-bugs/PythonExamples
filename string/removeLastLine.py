"""
编写一个函数
- 参数：一个字符串
- 返回值：原字符串删除最后一行后的新的字符串
"""


def remove_last_line(string):
    # 寻找到最后一个换行符的索引
    index_of_last_line_break = string.rfind('\n')

    # 通过切片返回新的字符串
    return string[:index_of_last_line_break]


if __name__ == '__main__':
    s = "hello \n world \n !"
    print(s)

    print(remove_last_line(s))
