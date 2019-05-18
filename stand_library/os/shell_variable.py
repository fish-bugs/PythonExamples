"""
读取所有shell变量
"""

import os

for key, value in os.environ.items():
    print("%s : %s" % (key, value))

print(os.environ["PATH"])
