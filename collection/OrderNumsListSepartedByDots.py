"""
一直一个列表形如：
  L = ['1.1.1.', '1.1.12.', '1.1.13.', '1.1.2.', '1.1.3.', '1.1.4.']

要求编写一个函数来让它排序
排序规则版本号
- 1.1.1 > 0.9.9
- 2.5.3 > 2.3.99

"""


def sort_nums_list(nums_list):
    def rule(item):
        return [p for p in item.split('.')]

    return sorted(nums_list, key=rule)


if __name__ == "__main__":
    list1 = ['3.1.1.', '1.41.12.', '1.1.13.', '71.1.2.', '1.13.3.', '1.1.4.']

    print(sort_nums_list(list1))
