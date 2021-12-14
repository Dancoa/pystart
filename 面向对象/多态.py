# 写一个函数，基类作为参数，子类复写基类中的函数，实例中当子类作为参数传入此函数，调用复写的方法时，会使用子类的那个函数
# 这就是多态


class person:
    def talk(self):
        print("我是父类啊！")
    
class teacher(person):
    def talk(self):
        print("我是子类teacher")
class student(person):
    def talk(self):
        print("我是子类student")

def starttalk(person):
    person.talk()

tony = student()
starttalk(tony)

danco = teacher()
starttalk(danco)

people = person()
starttalk(people)