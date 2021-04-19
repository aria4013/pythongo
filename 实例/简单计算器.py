# 方法1

class oper:
    oper=""
    func=""
    def __init__(self,oper):
        self.oper=oper.strip()

    def opers(self,num1,num2):
        swicher={
            '+':'jia',
            '-':'jian',
            '*':'cheng',
            '/':'chu',
        }
        func=swicher.get(self.oper,'default')
        if func == 'default':
            print('运算符错误')
            exit()
        num1=float(num1)
        num2=float(num2)
        func=getattr(self,func)
        return func(num1,num2)

    def jia(self,num1,num2):
        return num1 + num2

    def jian(self,num1,num2):
        return num1 - num2

    def cheng(self,num1,num2):
        return num1 * num2

    def chu(self,num1,num2):
        return num1 / num2


import re

print("例如：2+2，自动计算结果")
nums=input("请输入：")
numsObj=re.search(r'(\d+)(.*?)(\d+)',nums,re.M)
if numsObj:
    num1=numsObj.group(1)
    fuhao=numsObj.group(2)
    num2=numsObj.group(3)
    operObj=oper(fuhao)
    res=operObj.opers(num1,num2)
    print('运算结果{}'.format(res))
else:
    print("输入错误，{}".format(nums))

# 方法2

def divide(x, y):
    if y == 0:
        return '分母不能为0, 计算无效'
    else:
        return x / y
judge = True
symbol = {'1': '+', '2': '-', '3': '×', '4': '÷'}
while judge:
    def counter(x, y, num):
        expression = {'1': x + y, '2': x - y, '3': x * y, '4': divide(x, y)}
        if type(expression[num]) == int or type(expression[num]) == float:
            return '{}{}{}={}'.format(x, symbol[num], y, expression[num])
        else:
            return expression[num]
    print('选择运算：1、相加 2、相减 3、相乘 4、相除')
    chose = input('请输入你的选择（1/2/3/4）：')
    num1 = int(input('请输入第一个数字：'))
    num2 = int(input('请输入第二个数字：'))
    print('计算结果：',counter(num1, num2, chose))
    print('是否离开程序：是（Y） 否（N）')
    choice = input('请选择：')
    if choice == 'Y':
        judge = False
print('程序结束！')