# 1，2，3，4个数字，能组成多少个互不相同且无重复数字的三位数，输出
sum = 0
for i in range(1,5):
    for a in range(1,5):
        if i == a:
            continue
        for b in range(1,5):
            if i == b or a == b:
                continue
            sum = sum + 1
            print((str(i)+str(a)+str(b)))
            print("共有：",sum,"个")

# 这个方法牛批
uni = 0
list = [1,2,3,4]
for i in list:
    list1 = list.copy()
    list1.remove(i)
    for j in list1:
        list2 = list1.copy()
        list2.remove(j)
        for k in list2:
            uni += 1
            print(i,j,k,uni)
