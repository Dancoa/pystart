# 写入字符串."r+" 打开文件，在开头部分开始写，完成替换功能；"w+"打开文件，删除原有内容，从开头开始写
with open('/Users/danco/Desktop/pystart/文件操作/file.txt','w',encoding = 'utf-8') as f:
    f.write('okokokfgfgdsgsdg')

# 向文件写入一序列的字符串，序列可以是列表、元组、字典、集合等
x = open('/Users/danco/Desktop/pystart/文件操作/file.txt','r')
y = open('/Users/danco/Desktop/pystart/文件操作/file2.txt','w')
y.writelines(x.readlines())         # 实现了复制粘贴操作
x.close()
y.close()