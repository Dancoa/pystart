#!/usr/bin/python

# 输出1-10内的奇数
x = 1
while x < 10:
    if x % 2 == 1:
        print(x)
    x = x + 1
 
 # 1-100内被7整除的数输出
x = 1
while x < 100:
    if x % 7 == 0:
         print(x)
    x = x + 1

# 将列表中奇数偶数值区分开
# 第一种
a = [3242,13,456,7564,24,1,43,75]
even = []
odd = []
i = 0
while i < len(a):
    if a[i] % 2 == 0:
        even.append(a[i])
    else:
        odd.append(a[i])
    i += 1
print(even)
print(odd)

# 第二种
a = [3242,13,456,7564,24,1,43,75]
even = []
odd = []
while len(a) > 0:
    n = a.pop()
    if n % 2 == 0:
        even.append(n)
    else:
        odd.append(n)
print(even)
print(odd)


