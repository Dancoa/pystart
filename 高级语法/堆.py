# 堆的特点：
# 1.堆是个二叉树，父节点总是小于等于子节点
# 2.设父节点的序号为k，则满足左孩子序号为2k+1，右孩子序号为2k+2
# 3.最小的元素总是在根节点heap[0]

# 构造一个堆,使用heapq.heapqify()
import heapq
x = [2,35,5,42,25,6,34,8,4,1]
heapq.heapify(x)
print(x)

# 向堆里加入值（会保持堆的不变性），使用heapq.heappush()
heapq.heappush(x,33)
print(x)

# 弹出堆中最小的元素,使用heapq.heappop()
heapq.heappop(x)
print(x)

# 先加入，再弹出
w = heapq.heappushpop(x,56) # w的值为弹出的最小值，若加入的是最小值，则会将这个最小值弹出来
print(w)
print(x)

# 先弹出，再加入
y = heapq.heapreplace(x,-1) # y的值为还没加入前的最小值
print(y)
print(x)

# 将多个已排序的输入合并为一个已排序的输出
x = [2,4,5,6,7,32,45,76,453,657]
y = [1,3,7,8,45,345]
z = heapq.merge(x,y)
print(list(z))

# 从iterable所定义的数据集中返回前n个最大元素构成的列表
x = [2,4,5,6,7,32,45,76,453,657]
max = heapq.nlargest(3,x)
print(max)
# 从iterable所定义的数据集中返回前n个最小元素构成的列表
min = heapq.nsmallest(3,x)
print(min)

