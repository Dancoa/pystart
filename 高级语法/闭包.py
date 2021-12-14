# 闭包的特点：
# 1.函数里还有函数
# 2.内函数会用到外函数的变量
# 3.外函数的返回值是内函数

# 例子：买水果，称重量算价
def price(unitprice):
    def computer(weight):
        return (weight-0.1)*unitprice
    return computer
apple = price(3)        # 由于price函数的返回值为内函数computer，这里相当于apple=computer函数
print(apple(3.5))

