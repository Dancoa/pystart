# 输出一个九九乘法表
for i in range(1,10):
    for j in range(1,10):
        if j < i:       # 去除重复的项
            continue
        k = i*j
        print('%d * %d = %d'%(i,j,k),end=" ")   # end=，取消换行
    print()             # 换行目的是为了显示出阶梯的效果

    
print()

# 其他方法
num1 = 1
while num1 <= 9:
    num2 = 1
    while num2 <= num1:
        print('%d * %d = %d'%(num2,num1,num1*num2),end=" ")
        num2 = num2 + 1
    print()
    num1 = num1 + 1

        

