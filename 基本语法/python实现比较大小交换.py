#!/usr/bin/python
# 实现比较两个数大小，输出总是从小到大
x = 999
y = 888
if x > y:
    x,y = y,x
print(x,y)

# 计算四个数值中的最大值(mapreduce)
x = 123
y = 654
a = 5634
b = 3214
if a < b:
    a,b = b,a
if x < y:
    x,y = y,x
if a < x:
    a,x = x,a
print(a)
