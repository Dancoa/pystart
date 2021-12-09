#!/usr/bin/python

# os模块，提供了与操作系统交互的函数
import os
print(os.getcwd()) # 获取当前工作路径

# sys模块，提供了系统相关的参数和函数
import sys
print(sys.argv) # 输出一个包含当前正在执行文件的列表
print(sys.platform) # 输出当前的操作系统平台
print(sys.path) # 输出python解释器自动查找所需模块的路径的列表

# time模块，提供与时间相关的函数
import time
print(time.time()) # 输出当前时间，单位是秒
time.sleep(1) # 执行这条语句时，会等待1秒，再执行后面语句
print(time.localtime()) # 返回当前时间，time.struct_time元组

# math模块，提供对浮点数学的底层C库函数的访问
import math
x = math.cos(math.pi / 2) # 计算sin()和cos()
y = math.sin(math.pi / 2)
print(x,y)

