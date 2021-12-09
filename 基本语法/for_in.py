#!/usr/bin/python

# 同时遍历列表、元组的索引和值，使用enumerate函数
a = ["python","人工智能","大数据"]
for x,y in enumerate(a):
    print(x,y)
b = ("佐菲","泰罗","初代")
for m,n in enumerate(b):
    print(m,n)

# items()返回字典内的键值对
# keys()返回字典内所有key列表
# values()返回字典中所有value列表
a = {
    "danco":99,
    "alex":98,
    "oreo":97
}
for x,y in a.items():
    print(x,y)
for x in a.keys():
    print(x)
for y in a.values():
    print(y)

# 遍历字符串
s = "python"
for x in s:
    print(x,end="-")

# 构造一个列表，将其中的正数输出
a = [123,324,-123,0,324,-23,-324,23,-324]
for x in a:
    if x > 0:
        print(x)

# range()可以生成一个可迭代对象
a = range(1,9,2) # 从1到9， 不包括9 ，步长为2
print(a)
b = list(a) # 把可迭代对象转为一个列表
print(b)
# 计算1-100的和
su = 0
for x in range(1,101):
    su = su + x
print(su)

print(sum(range(1,101))) # 用sum()函数直接计算



