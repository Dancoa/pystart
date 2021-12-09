#!/usr/bin/python

# 有返回值，函数运行结果就是一个值
# 无返回值，直接调用函数，执行函数
def area1():
    return 3.14 * 2 * 2
def area2(r):
    return 3.14*r*r
def area3(r):
    print(3.14*r*r)
print(area1())
print(area2(2))
area3(3)

