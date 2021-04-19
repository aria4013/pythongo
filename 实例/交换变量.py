# 方法1
# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : www.runoob.com
 
# 用户输入
 
x = input('输入 x 值: ')
y = input('输入 y 值: ')
 
# 不使用临时变量
x,y = y,x
 
print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))

# 方法2
# -*- coding: UTF-8 -*-

# 用户输入
x = int(input('输入 x 值: '))
y = int(input('输入 y 值: '))

x = x + y
y = x - y
x = x - y

print('交换后 x 的值为: {}'.format(x))
print('交换后 y 的值为: {}'.format(y))

# 方法3
#交换变量
x = int(input('输入 X 值：'))
y = int(input('输入 Y 值：'))
x = x ^ y
y = x ^ y
x = x ^ y
print('交换后的 X 值为：',x)
print('交换后的 Y 值为：',y)