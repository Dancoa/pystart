# 栈：先进后出，filo
# 队列：先进先出，fifo

# 栈的实现
x = [1,2,3]
x.append(666)
print(x)
x.pop()
print(x)


# 队列的实现
from collections import deque
x = deque([7,8,9])
print(x)
x.append(666)
print(x)
x.popleft()
print(x)
