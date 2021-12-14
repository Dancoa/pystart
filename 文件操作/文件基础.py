# 与文件处理相关的模块
# OS:提供了大量操作文件、目录的方法
# pathlib2:文件系统路径操作
# openpyxl:操作Excel文件
# python-docx:操作Word文件
# python-pptx:操作ppt
# opencv-python:图像处理模块

#  打开文件
#  open(file,mode='x')
#  file:必需，文件路径（相对或绝对）
#  mode:文件打开模式
#  'r':读
#  'w':写
#  'a':在文件尾部追加内容(append)
#  'b':二进制文件(图像文件，binary)
#  't':文本文件(text)
#  '+':复合(r+ 读写，写时从头开始覆盖；w+ 读写，清空源文件后读写)

#  关闭文件，使用open方法一定要保证关闭文件对象
#  file.close()
#  使用with...as...隐式调用close()方法关闭文件，即在对文件进行操作之后，自动关闭，无需再调用open方法
#  with open('file.txt','r') as f:


#  判断文件是否关闭
#  file.closed
f = open('/Users/danco/Desktop/pystart/文件操作/file.txt','r')
print(f.closed)
f.close()
print(f.closed)

# 用with open as的优点在于，在其外部执行其他语句时，他已经自动关闭了，无需使用x.close再关闭了
with open('/Users/danco/Desktop/pystart/文件操作/file.txt','r') as x:
    print(x.name)
    print(x.mode)
    print(x.encoding)
    print(x.closed)
print(x.closed)

