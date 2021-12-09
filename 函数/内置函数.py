#!/usr/bin/python
 
# 对可迭代对象的处理；可迭代对象，简单来说就是可以用for循环的对象
# list构造列表，set构造集合，tuple构造元组，dict构造字典
a = range(10)
b = list(a)
c = tuple(a)
d = set(a)
e = dict(开发=1,运维=2,测试=3,算法=4)
print(a,"\n",b,"\n",c,"\n",d,"\n",e)

# 数学运算
x = [43,45,23,6,7,23,75,3,2,98]
print(min(x))
print(max(x))
print(sum(x))

# 排序sorted,从小到大;并不会改变原对象
x = [5,345,35,53,53,5,65465,7,54,32]
y = sorted(x)
print(x,"\n",y)

# zip()函数，将可迭代对象作为参数，将对象中的元素一一对应组合，打包成一个个元组(无法直接输入，需转换成list\set\tuple\dict)
x = [42,4253,63,2]
y = [324,426,76]
z = zip(x,y)
print(z)
print(dict(z))

# all()用于判断给定的可迭代函数iterable中的所有元素是否都为true，若是返回true,不是返回false
# ant()用于判断给定的可迭代函数iterable中的所有元素是否都有true,若有返回true,没有返回false
# 0，空，None，False都是false
print(all([34,2,41431,4,1,413,21]))
print(all([45,3452,424,230,4,0,424,3]))
print(any([0,0,0,0,0,3,54,0,0,0]))
# 对于all()空元组、空列表返回值为true
# 对于any()空元组、空列表返回值为false
print(all([]))
print(any([]))

