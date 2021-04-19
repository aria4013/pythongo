# 方法1
# -*- coding: UTF-8 -*-
 
# Filename : test.py
# author by : www.runoob.com
 
# 九九乘法表
for i in range(1, 10):
    for j in range(1, i+1):
        print('{}x{}={}\t'.format(j, i, i*j), end='')
    print()

# 方法2
for i in range(1, 10):
    for j in range(1, i + 1):
        if i == j:
            print('{1}×{0}={2}'.format(i, j, i * j))
        else:
            print('{1}×{0}={2}'.format(i, j, i * j), end='\t')

# 方法3
print('\n'.join(' '.join("%dx%d=%-2d" % (x, y, x*y) for x in range(1, y+1)) for y in range(1, 10)))