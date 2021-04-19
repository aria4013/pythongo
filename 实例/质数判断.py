# 用平方根算法减少时间
import math
# 用户输入数字
num = int(input("请输入一个数字: "))
# 质数大于 1
if num > 1:
    #因为向上向下取整的函数对于整数来说都是自身，所以要想查找因子必须+1来包括自身
    #所以用的是向下取整函数，否则向上取整后比如平方根是5.2>>6>>7多算一个6
    pingfanggeng = math.floor( num ** 0.5 )
    # 查找其因子
    for i in range(2, pingfanggeng+1): #向下取整后需要加一来判断平方根位的因数，包括平方根
        if (num % i) == 0:
            print(num, "是合数")
            print(i, "乘于", num // i, "是", num)
            break
    else:
        print(num, "是质数")
        # 如果输入的数字小于或等于 1，那就不是质数
else:
    print(num, "既不是质数，也不是合数")