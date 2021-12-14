# 构造一个基类学生，包含学习方法
# 构造继承类计算机专业学生，包含方法编程
# 构造继承类金融专业学生，包含方法金融交易

## 类的方法的第一参数必须是self
## 举例解释原理：创建了一个MyClass类，实例化得到MyObject这个对象，然后调用这个类的方法MyObject.method(arg1,arg2)
## 在这个过程中，Python会自动转为MyClass.method(MyObject,arg1,arg2)
class student:
    def __init__(self,name):
        self.name = name

    def study(self):
        print("我热爱学习！")

class csstudent(student):
    def programming(self):
        print("我爱编程！")

class ecostudent(student):
    def skill(self):
        print("我爱金融！")

bill = csstudent("Bill")
bill.programming()
bill.study()

tony = ecostudent("Tony")
tony.study()
tony.skill()