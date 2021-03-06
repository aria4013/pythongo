# 方法1

#!/usr/bin/python3
 
# Filename : test.py
# author by : www.runoob.com
 
# 通过用户输入数字计算阶乘
 
# 获取用户输入的数字
num = int(input("请输入一个数字: "))
factorial = 1
 
# 查看数字是负数，0 或 正数
if num < 0:
   print("抱歉，负数没有阶乘")
elif num == 0:
   print("0 的阶乘为 1")
else:
   for i in range(1,num + 1):
       factorial = factorial*i
   print("%d 的阶乘为 %d" %(num,factorial))

# 方法2
# 查了一下 math 库的帮助，发现自带阶乘函数。所以代码可以简洁一点。
# -*- coding: UTF-8 -*-

# Filename : factorial.py
# author : Pt

import math
num = int(input("请输入一个数字："))
if num < 0:
    print("负数是没有阶乘的！")
else:
    print("{0} 的阶乘为 {1}".format(num, math.factorial(num)))