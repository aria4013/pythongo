# 方法1
#!/usr/bin/python
# -*- coding:utf-8 -*-

a = int(input('摄氏度转换为华氏温度请按1\n华氏温度转化为摄氏度请按2\n'))
while a != 1 and a != 2:
    a = int(input('你选择不正确，请重新输入。\n摄氏度转换为华氏温度请按1\n华氏温度转换为摄氏度请按2\n'))
if a == 1:
    celsius = float(input('输入摄氏度:'))
    fahrenheit = (celsius*1.8)+32 #计算华氏温度
    print('%.1f摄氏度转为华氏温度为%.1f' %(celsius,fahrenheit))
else:
    fahrenheit = float(input('输入华氏度:'))
    celsius = (fahrenheit - 32)/1.8 #计算摄氏度
    print('%.1f华氏度转为摄氏度为%.1f' %(fahrenheit,celsius))

# 方法2
a = input("请输入带有符号的温度值: ")
if a[-1] in ['F','f']:
    C = (eval(a[0:-1]) - 32)/1.8
    print("转换后的温度是{:.1f}C".format(C))
elif a[-1] in ['C','c']:
    F = 1.8*eval(a[0:-1]) + 32
    print("转换后的温度是{:.1f}F".format(F))
else:
    print("输入格式错误")