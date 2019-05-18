"""
如何判断一个数字是不是一个平方数？
- 16 => True
- 18 => False
"""

def is_square(apositiveint):
  x = apositiveint // 2
  seen = set([x])
  while x * x != apositiveint:
    x = (x + (apositiveint // x)) // 2
    if x in seen: return False
    seen.add(x)
  return True

for i in range(110, 130):
   print(i, is_square(i))
