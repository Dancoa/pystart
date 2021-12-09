#!/usr/bin/python

# 列表
x = [1,2,3,4,5,6,7,8,9,10]
# 获取最后5个
print(x[5:])
print(x[-5:])
# 增加个666
x.append(666)
print(x)
# 删除最后一个
del x[10]
print(x)

# 元组
a = (3,4,6,2,7,3,8)
print("a=",a)
# 元组为单元素时，在单元素后要加逗号
b = (5)
c = (5,)
print("b=",b)
print("type(b)",type(b))
print("c=",c)
print("type(c)=",type(c))
# 访问元素，与列表一样
print(a[4:])
print(a[3])
# 删除,无法删除元组中元素，但能删除整个元组；元组中的元组都无法更改
del a
# 连接操作
x = (3,4,5)
y = (7,8,9)
print(x+y)
# 计算元组元素个数
x = (2,42,42,34,23,42,5,6,5474,7,46,36,"fjkgfd")
print(len(x))
# 元组的迭代
x = (5,6,7)
print(x*3)

# 字典;它就是键值对;不区分单双引号;它是无序的
d = {
    "danco":1,
    "alex":2,
    "kudo":3
}
print(d)
# 引用和赋值
print(d)
print(d["danco"])
d["kudo"] = 4869
print(d)
# 增加,删除值
d["oreo"] = 999
print(d)
del d["kudo"]
print(d)

# 集合;两种创建方式：
x = {45,64654,445,45,6771}
print(x)
y = set([1,2,3,4,7,8,9])
print(y)
# 不允许重复值存在
z = [1,1,2,2,3,3]
t = set(z)
print(t)
# 向集合内添加元素
t.add(4869)
print(t)

# 删除一个元素
h = set((1,7,8,2,6,4,5)) 
h.pop() # 集合为数字，删除最小值；集合为字符串，随机删除
h.pop()
print(h)
g = set(('sf','sdfas','sdf','sdfafddf'))
g.pop()
print(g)
# 删除指定元素
b = set((2,3,5,6,3,2))
b.remove(2)
print(b)
# 删除全部元素
b.clear()
print(b)
# 删除集合
del b
# 交集& 并集| 差集-
a = set((1,3,4,6,8,9))
b = set((3,5,6,7,8,9))
a1 = a & b
a2 = a | b 
a3 = a - b
print(a1,a2,a3)