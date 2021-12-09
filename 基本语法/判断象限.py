#!/usr/bin/python

# 判断象限
x = int(input("请输入x值:"))
y = int(input("请输入y值:"))
if x != 0 and y != 0:
    if x > 0 and y > 0:
      g = 1
    elif x > 0 and y < 0:
        g = 4
    elif x < 0 and y > 0:
        g = 2
    elif x < 0 and y < 0:
        g = 3
    print("坐标在第%d象限"%(g))
else:
    print("坐标位于坐标轴")
    
