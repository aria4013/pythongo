#-*- coding UTF-8 -*-
#author by:Lebron
a=[]
while True:
    #输入q来结束输入数字
    print('输入q结束')
    c=input('请输入数字：')
    if c!='q':
        try:
            i=int(c)
            a.append(i)
        except ValueError:
            print('输入的不是数字')
    else:
        break
print('最大数字是：',max(a))