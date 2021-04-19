# 方法1
def gcd(a, b):
    if b > a:
        a, b = b, a   # b为最小值
    if a % b == 0:
        return b      # 判断b是否为最大公约数
    for i in range(b//2+1, 1, -1):    # 倒序求最大公约数更合理
        if b % i == 0 and a % i == 0:
            return i
    return 0

while(True):
    a = int(input("Input 'a':"))
    b = int(input("Input 'b':"))
    print(gcd(a, b))

# 方法2
def gcd(x, y): # very fast
   return x if y == 0 else gcd(y, x%y)

print(gcd(378, 5940))  # result: 54

# 方法3
# 欧几得里算法的完善版，输入任意两个整数，求最大公约数。
def gcd(a,b):
    if a == 0:
        a,b = b,a
    while b != 0:
        a,b = b,a%b
    return a

c = int(input('请输入第一个正整数: '))
d = int(input('请输入第二个正整数: '))

if c>d:
   b = d
else:
   b = c

print('{}和{}的最大公约数为: {}'.format(c,d,gcd(c,d)))

# 方法4
# 辗转相除法(不用判断大小)
def f1(a,b):
    while b!=0:
        a,b=b,a%b
    print(a)
f1(27,6)

# 相减法
def f2(a,b):
    while a!=b:
        a,b=min(a,b),abs(a-b)
    print(a)
f2(27,6)

# 方法5
# 使用 math 模块的 gcd()
import math

a = 54
b = 24
print(math.gcd(a, b))