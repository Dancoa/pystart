# 函数read()，逐个字节或字符读取文件中的内容，有参数时，读取参数个字节或字符
with open('/Users/danco/Desktop/pystart/文件操作/file.txt','r') as f:
    # print(f.read(2))

# readline()，读一行，会自动换行。加上参数时若参数大于一行字符总数，则输出一整行并换行；若参数小于字符总数，则输出参数个字符
    print(f.readline(3))

# readlines()，以列表的形式读出每一行,若加上参数，会以列表的形式输出参数个字符串
    print(f.readlines(6))


# 格式控制例子
# 源文件
with open('/Users/danco/Desktop/pystart/文件操作/file.txt','r') as x:
    for i in x.readlines():
        print(i,end="")
    print('=================')
# 格式转换
from datetime import datetime
file = "/Users/danco/Desktop/pystart/文件操作/file.txt"
with open(file,'r') as y:
    for line in y.readlines():
        mydate,pri = line.split(",")   # 以逗号分隔，将逗号两边的字符分别赋值给mydate和pri
        dt = datetime.strptime(mydate,'%Y/%m/%d')      # datetime.strptime是将字符串转换为年-月-日 时-分-秒的格式
        pri = float(pri)
        print("时间："+str(dt.date())+"数量："+str(pri))