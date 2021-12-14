#  变量类型：
#  1.系统变量：__xxx__,是特殊变量
#  2.保护变量：_xx,可以被访问，通常视为私有变量，不要随意访问
#  3.私有变量：__xx，私有变量，无法直接使用

class person:
    def __init__(self,name,age):
        self.name = name
        self.__age = age

    def show(self):
        print("姓名是：",self.name)
        print("年龄为：",self.__age)
    
    def setage(self,age):
        if age < 0:
            print("输入年龄有误")
        else:
            self.__age = age
# 先看看初始的值
danco = person("danco",23)
danco.show()

# 更改age的值，可以看到输出还是原来的值
danco.age = 89
print(danco.age)    # 这里能输出，相当于给danco对象新加了一个变量age
danco.show()

# 通过setage方法更改age,修改成功
danco.setage(24)
danco.show()

# 直接修改__age，可以看到修改失败
danco.__age = 25
danco.show()

# 使用对象._类名__私有变量名 ，修改成功。但一般强烈不建议去修改私有变量
danco._person__age = 25
danco.show()