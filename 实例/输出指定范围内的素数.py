#输出指定范围内的素数
#非数字字符串会出错，一开始就应该避免错误的发生（限定范围），而不是报错了再来改进，
#可以继续改进用列表输出质数和合数
import math
lower = int(input("输入区间(包括)最小值: "))
upper = int(input("输入区间(包括)最大值: "))
sumzs=0
sumhs=0
print("素数结果如下：")
print("="*10)

pri_num = 0
com_num = 0

for num in range(lower, upper + 1):
    if num > 1:    # 素数大于 1
        square_num = math.floor(num ** 0.5)    # 找到其平方根，减少算法时间
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
        for i in range(2, (square_num + 1)):  #（2,2）属于空集，不会出错，但也不会执行
            if (num % i) == 0:  #可以被整除说明是合数
                com_num += 1
                sumhs+=num
                print(num,"是合数")
                break   #执行到这里说明是合数，跳出里层for和所有else语句，执行完其他语句（比如下面注释掉的）后继续外一层for的下一次循环
            else:       #不能被依次整除，说明循环完了还是质数，用pass表示占位
                pass    #继续执行下一句else语句
#这里的else和上面的for属于一个级的，能执行下面的语句说明上面的质数筛选已经过关了，没有执行break。           
        else:                  #上面的for模块执行完了，说明都不能被2到平方根的数整除
            pri_num += 1        #所以质数计数+1
            sumzs+=num
            print(num,"是质数")
#        print(num,"是质数")       #这就是break执行后继续执行的语句，同for和else级别，也就是上面说的其他语句
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++ 
    else:
        print(num,"既不是素数也不是合数")
print("="*10)
print(com_num,'个合数','和为',sumhs)
print(pri_num,'个素数','和为',sumzs)