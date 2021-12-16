# 计算 3+33+333+3333+......
init_num = input("请输入数值:")
n = int(input("请输入位数:"))
list = []
sum = 0
for i in range(1,n):
    list.append(i*'3')
for a in list:
     sum = sum + int(a)
print(list)
print(sum)

# 另一种方法
init_num1 = int(input("请输入数值:"))
n1 = int(input("请输入位数:"))
sum1 = 0
num1 = 0
for i in range(n1):
    num1 = num1 + init_num1 * (10 ** i)
    sum1 = sum1 + num1

print(sum1)