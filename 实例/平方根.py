# 正数

# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : www.runoob.com
 
num = float(input('请输入一个数字： '))
num_sqrt = num ** 0.5
print(' %0.3f 的平方根为 %0.3f'%(num ,num_sqrt))

# 负数和复数

# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : www.runoob.com
 
# 计算实数和复数平方根
# 导入复数数学模块
 
import cmath
 
num = int(input("请输入一个数字: "))
num_sqrt = cmath.sqrt(num)
print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(num ,num_sqrt.real,num_sqrt.imag))

# 复数
#!/usr/bin/python3

import cmath

a = float(input("请输入一个实数字: "))
b = float(input("请输入一个虚数字: "))
num_sqrt = cmath.sqrt(complex(a, b))
print('{0:0.3f}+ {1:0.3f}j 8的平方根为 {2:0.3f}+{3:0.3f}j'.format(a, b, num_sqrt.real, num_sqrt.imag))

# 除long外
def sqrt():
  
  import cmath
# # 计算实数和复数平方根# # 导入复数数学模块 isinstance(num ,  (float,int) )
  num = input('输入第一个数字：')
  if num.__contains__('-') and  num.__contains__('.'):  # 负数、浮点数    
    num_sqrt = cmath.sqrt(float(num))
    print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(float(num), num_sqrt.real, num_sqrt.imag))
  elif num.__contains__('-'):  # # 负数、整数    
    num_sqrt = cmath.sqrt(int(num))
    print('{0} 的平方根为 {1:0.3f}+{2:0.3f}j'.format(int(num), num_sqrt.real, num_sqrt.imag))
  else:
    if num.__contains__('.'):   # 非负数、浮点数 整数        
       num_sqrt = float(num) ** 0.5        
       print(' %0.3f 的平方根为 %0.3f' % (float(num), num_sqrt))
    else:   #  # 非负数、整数       
      num_sqrt = int(num) ** 0.5        
      print(' %0.3f 的平方根为 %0.3f' % (int(num), num_sqrt))