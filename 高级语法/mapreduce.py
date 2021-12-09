# map函数，其根据提供的函数对指定的序列做映射，返回值为iterators类型，需要用list转换
def square(x):
    return x*x
a = [1,2,3,4,5,6,7]
b = map(square,a)
print(list(b))      

# # reduce函数
# # 过程：1.将序列前两个元素作为初始值带入函数计算
#        2.将第一步计算结果作为函数的一个参数，后续元素为第二个元素继续带入函数计算
#        3.以此类推
from functools import reduce
def compare(x,y):
    z = x if x > y else y
    return z
xulie = [234,5645,424,13,14,3,42,432,424,4]
result = reduce(compare,xulie)
print(result)

# 计算6！
from functools import reduce
def jiecheng(b,c):
    a = b*c
    return a
x = list(range(1,7))
y = reduce(jiecheng,x)
print(y)