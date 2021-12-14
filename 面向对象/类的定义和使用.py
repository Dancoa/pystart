# 举个例子
class guaishou:
    def __init__(self,name,weight,height):
        # __init__方法是初始化类的方法，其必须包含self参数,__init__函数不是必须的
        print("开始变身")
        self.name = name
        self.weight = weight
        self.height = height
        print("变身结束！")

    def kill(self):
        # 这是实例方法，必须包含self参数
        print("我的刀正在饮血！")
galulu = guaishou("加鲁鲁兽",100,120)
galulu.kill()
print(galulu.name)
print(galulu.height,galulu.weight)

# 构造一个学生类，包含身高、体重属性，“学习”方法
class student:
    def __init__(self,height,weight):
        self.height = height
        self.weight = weight

    def study(self):
        print("good study")

zhangsan = student(60,178)
print(zhangsan.height)
print(zhangsan.weight)
zhangsan.study()