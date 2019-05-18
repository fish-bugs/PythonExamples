def interleave(list1, list2):
    return [val for pair in zip(list1, list2) for val in pair]


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

if __name__ == "__main__":
    print(interleave(list1, list2))
    # [1, 'a', 2, 'b', 3, 'c']

"""
大家可以运行下结果，看看有没有实现功能。
是不是很舒服，只要一行代码

- 首先是用zip进行压缩
- 然后一个列表推导式把它展开
- 然后又跟着一个列表推导式把它给展开

"""
