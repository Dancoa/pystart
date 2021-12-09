# 自己调用自己时__name__==__main__，否则不是
def x():
    if __name__ == '__main__':
        print("自己调用自己")
    else:
        print("别人在调用")

def y():
    a = 'hahaha'
    print('haha',a)