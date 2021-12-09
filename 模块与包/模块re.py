# re模块，为高级字符串处理提供了正则表达式工具
import re

# re.search(pattern,string) 在字符串中寻找模式,输出找到的第一个的位置
x = "python is very interesting,Python is so good!"
print(re.search("is",x))

# re.match(pattern,string) 在字符串开始处匹配模式，如果一开始没匹配到就输出none
print(re.match("is",x))

# re.split(pattern,string) 根据模式分割字符串
print(re.split("i",x))

# re.finall(pattern,string) 列表形式返回匹配项
print(re.findall("[Pp]",x))

# re.compile(pattern) 创建模式对象,即先将我们要匹配的模式固定，然后直接用对象调用函数
r = re.compile("[0-9]")
x = "今天是2021年12月9号"
print(r.match(x))
print(r.search(x))
print(r.findall(x))
