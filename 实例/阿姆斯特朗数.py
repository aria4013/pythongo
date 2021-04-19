# 如果一个n位正整数等于其各位数字的n次方之和,则称该数为阿姆斯特朗数。 例如1^3 + 5^3 + 3^3 = 153。

# 1000以内的阿姆斯特朗数： 1, 2, 3, 4, 5, 6, 7, 8, 9, 153, 370, 371, 407。

# 以下代码用于检测用户输入的数字是否为阿姆斯特朗数：

# Filename : test.py
# author by : www.runoob.com
 
# Python 检测用户输入的数字是否为阿姆斯特朗数
 
# 获取用户输入的数字
num = int(input("请输入一个数字: "))
 
# 初始化变量 sum
sum = 0
# 指数
n = len(str(num))
 
# 检测
temp = num
while temp > 0:
   digit = temp % 10
   sum += digit ** n
   temp //= 10
 
# 输出结果
if num == sum:
   print(num,"是阿姆斯特朗数")
else:
   print(num,"不是阿姆斯特朗数")

# 输出指定区间内的所有阿姆斯特朗数
try:
    lower = int(input("最小值："))
    upper = int(input("最大值："))
except ValueError:
    print("所输入内容非整数!")
    exit(1)

for num in range(lower, upper+1):
    sum = 0
    n = len(str(num))
    
    for i in str(num):
        sum += int(i) ** n
    
    if sum == num:
        print(num)