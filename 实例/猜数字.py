# while 无限循环法
# 随机生成一个1~100中的数字

# 导入 random(随机数) 模块
import random

num = random.randint(1,100)

# 判断输入的是否为整数数字
cainum = int(input("请输入您猜的数字："))

while True :  # 无限循环
    if (num > cainum) :
        print ("您猜的数字", cainum, "比生成的数字小")
        cainum = int(input("请再次输入您猜的数字："))

    if (num < cainum) :
        print ("您猜的数字", cainum, "比生成的数字大")
        cainum = int(input("请再次输入您猜的数字："))

    if (num == cainum) :
        print ("恭喜您猜中数字：", cainum)
        break # 猜中数字后跳出循环

# 递归法
# 导入 random(随机数) 模块
import random

num = random.randint(1,100)

def cai(cainum) :
    if (num > cainum) :
        print ("您猜的数字", cainum, "比生成的数字小")
        cainum = int(input("请再次输入您猜的数字："))
        
    if (num < cainum) :
        print ("您猜的数字", cainum, "比生成的数字大")
        cainum = int(input("请再次输入您猜的数字："))
        
    if (num == cainum) :
        print ("恭喜您猜中数字：", cainum)
        return

    cai(cainum)

cainum = int(input("请输入您猜的数字："))
cai(cainum)