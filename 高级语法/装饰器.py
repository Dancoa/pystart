# 需求，写一个计算加减乘除的计算器，要求在计算前先输出一些=号
# 实际上就是闭包的应用

# def show(function):
#     def temp(a,b):
#         print("==========")
#         z = function(a,b)
#         return z
#     return temp

# def myadd(a,b):
#     return a+b

# jiafa = show(myadd)
# print(jiafa(1,2))

# 改进：使用修饰器语法糖：@
def show(function):
    def temp(a,b):
        print("==========")
        z = function(a,b)
        return z
    return temp

@show               # 这里的作用等价于myadd=show(myadd),即已将myadd函数作为参数传进了show函数中，myadd函数可以直接调用
def myadd(a,b):
    return a+b
@show
def mydel(a,b):
    return a-b

print(myadd(1,2))
print(mydel(4,3))

#设计一个装饰器，能计算圆和正方形面积
def showarea(function):
    def jisuan(size):
        print("=======现在开始计算面积==========")
        area = function(size)
        return area
    return jisuan

@showarea
def circle(size):
    return size**2*3.14

@showarea
def square(size):
    return size**2

print(square(3))
print(circle(3))

# 参数*args是元组，**kwargs是字典，参数数量都可任意
def zhuangshiqi(function):
    def jisuanqi(*args):
        print("=====这是一个计算器=====")
        x = function(*args)
        return x
    return jisuanqi

@zhuangshiqi
def jiafax(a,b,c,d,e):
    return a+b+c+d+e
@zhuangshiqi
def jianfa(a,b,c):
    return a-b-c
@zhuangshiqi
def chengfa(a,b):
    return a*b

print(jiafax(4,6,3,46,7))
print(jianfa(55,3,99))
print(chengfa(8,9))