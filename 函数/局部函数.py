#!/usr/bin/python
# 局部函数
from typing import Sequence


def my(type,n):
    def double(n):
        return n*2
    def add(n):
        return n+10
    def square(n):
        return n*n

    if type == "double":
       return double(n)
    if type == "add":
        return add(n)
    if type == "square":
        return square(n)
print(my("add",9))
print(my("double",7))
print(my("square",3))

# 匿名函数
def my2(type):
    if type == "double":
        return lambda n:n*2
    elif type == "add":
        return lambda n:n+9
    elif type == "square":
        return lambda n:n*n
    else:
        print("输入有误！")
fun1 = my2("double")
print(fun1(3))
fun2 = my2("add")
print(fun2(3))
fun3 = my2("square")
print(fun3(3))
