def interleave(*args):
    return [val for pair in zip(*args) for val in pair]


list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['github', 'google.com', 'so']

if __name__ == "__main__":
    print(interleave(list1, list2, list3))
    # [1, 'a', 'github', 2, 'b', 'google.com', 3, 'c', 'so']

"""
我们这次通过Python动态类型的特性，
传递*args作为参数而不是写死
使得我们的函数有无限扩张能力！
现在我们的interleave函数可以接受任意多个参数了
"""
