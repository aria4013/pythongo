# 方法1
# 最小公倍数
def lcm(a, b):
    if b > a:
        a, b = b, a     # a为最大值
    if a % b == 0:
        return a        # 判断a是否为最小公倍数
    mul = 2             # 最小公倍数为最大值的倍数
    while a*mul % b != 0:
        mul += 1
    return a*mul

while(True):
    a = int(input("Input 'a':"))
    b = int(input("Input 'b':"))
    print(lcm(a, b))

# 方法2
# 求两个数之间的最小公倍数相对简单，用两个数的乘积对两个之间的最大公约数求商即可:
def gcd(a,b):
    while (a!=0) & (b!=0):
        a,b = b,a%b
    return a

c = int(input('请输入第一个正整数: '))
d = int(input('请输入第一个正整数: '))
print('{}和{}的最小公倍数为: {}'.format(c,d,(c*d)//gcd(c,d)))

# 方法3
import math
a = 54
b = 24
print(a*b/math.gcd(a,b))

# 方法4
# 乘法解决：两个数分别取自己的乘积，直到相等。

lis = [int(input('输入数字1：')), int(input('输入数字2：'))]
a = b = 1
c, d = 0, 1

while True:
    if c < d:
        a += 1
        c = min(lis) * a
    elif c > d:
        b += 1
        d = max(lis) * b
    elif c == d:
        print('最小公倍数: %d'%c)
        break
# 除法解决：较大数取乘积，直到可被较小数整除时（反之亦可）

lis = [int(input('输入数字1：')), int(input('输入数字2：'))]
a = b = 1

while True:
    if a % min(lis) == 0:
        print('最小公倍数: %d' % a)
        break
    b += 1
    a = max(lis) * b