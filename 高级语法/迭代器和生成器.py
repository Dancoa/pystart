# 迭代器
x = ["xiangao","python","xman"]
y = iter(x)     # 在这里生成了一个对应于可迭代对象x的一个迭代器y
print(next(y))
print(next(y))
print(next(y))

# 生成器
def xen(n):
    for i in range(n):
        yield i+1       # 这里不能return，return只能生成一个值，yield生成的是一个可迭代对象
a = xen(3)
print(a)
for i in a:
    print(i)

# 用此方法也可以生成
gen = (i*i for i in range(6))
print(list(gen))

# 用生成器的意义.从输出可以看出，用生成器生成的可迭代对象所耗计算机的时间和空间都远小于直接构造;因为生成器产生的是对象，一个公式而已
import sys
import time
t1 = time.time()
mylist = [i for i in range(100000000)]
t2 = time.time()
print("占用时间:",t2-t1)
print("占用空间:",sys.getsizeof(mylist))

t3 = time.time()
mygen = (i for i in range(100000000))
t4 = time.time()
print("占用时间:",t4-t3)
print("占用空间:",sys.getsizeof(mygen))