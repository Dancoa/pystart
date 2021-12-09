#!/usr/bin/python

# 用局部函数实现
input1 = int(input("请输入第一个参数："))
input2 = int(input("请输入第二个参数："))
type = input("请输入计算类型：")
def computer(type,input1,input2):
    def add(input1,input2):
        return input1 + input2
    def dele(input1,input2):
        return input1 - input2
    def mul(input1,input2):
        return input1 * input2
    def devi(input1,input2):
        return input1 / input2
        
    if type == "+":
        return add(input1,input2)
    elif type == "-":
        return dele(input1,input2)
    elif type == "*":
        return mul(input1,input2)
    elif type == "/":
        return devi(input1,input2)
    else:
        return "目前只支持加减乘除！"
    
print(computer(type,input1,input2))
# 问题总结：程序从上往下执行，在调用函数时，一定要先定义，否则会报错

# 用匿名函数实现
input1 = int(input("请输入第一个参数："))
input2 = int(input("请输入第二个参数："))
type = input("请输入计算类型：")
def computer(type):
    if type == "+":
        return lambda input1,input2:input1+input2
    elif type == "-":
        return lambda input1,input2:input1-input2
    elif type == "*":
        return lambda input1,input2:input1*input2
    elif type == "/":
        return lambda input1,input2:input1/input2
    else:
        return "目前只支持加减乘除！"
fun = computer(type)
print(fun(input1,input2))