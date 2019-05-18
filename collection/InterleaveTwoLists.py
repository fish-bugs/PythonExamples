"""
如何合并两个长度相等的list？

示例：
- 输入：
  - list1： [1, 2, 3]
  - list2:  ['a', 'b', 'c']

- 输出：
  - [1, 'a', 2, 'b', 3, 'c']
"""


def interleave_by_loop(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("传入的list的长度需要相等")

    new_list = []
    for index, value in enumerate(list1):
        new_list.append(value)
        new_list.append(list2[index])
    return new_list


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']

if __name__ == "__main__":
    print(interleave_by_loop(list1, list2))
    # [1, 'a', 2, 'b', 3, 'c']

"""
上面给出了一个简单的示例，就是通过一次带有索引for循环
每次循环中将两个list中对应的元素插入新的list

但是如果我们要求合并三个、四个、五个lists呢？

我们可以按照Python风格来优雅的实现上述功能！
"""
