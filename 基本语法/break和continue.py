#!/usr/bin/python

# 输出列表里的第一个奇数
a = [324,234,536,23441,343,524,235]
for x in a:
    if x % 2 != 0:
        print(x)
        break

# continue意思是其后面的语句不再执行，继续回去循环
# 输出列表内的奇数
a = [324,234,536,23441,343,524,235]
for x in a:
    if x %2 ==0:
        continue
    print(x)

