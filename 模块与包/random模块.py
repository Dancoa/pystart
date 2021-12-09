# random模块， 提供了随机选择的一些函数
import random

# random.randrange(),从1-20（不包括20），步长为2，中随机选择1个数
print(random.randrange(1,20,3)) 
# random.randint(),从1-20（包括20）中随机选择1个数
print(random.randint(1,20)) 

# random.choice(),从非空序列随机返回一个元素
x = ["ssdf","sdfgg","sdfssaad","dfs","sffaggcv"]
print(random.choice(x)) 

# random.shuffle(),会将序列顺序重新随机排列
# 这里需注意，random.shuffle()函数没有返回值（None），他是直接将序列本身更改
y = list(range(100))
print(y)
random.shuffle(y)     
print(y)              

# random.sample()函数，从序列中随机选取k个。多用于从多样本中取样
a = ["danco","alex","oreo","kudo"]
b = random.sample(a,3)    
print(b)

# 产生0-1之间的随机浮点数
print(random.random()) 
# 产生9-11之间的随机浮点数 
print(random.uniform(9,11)) 