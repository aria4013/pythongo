#!/usr/bin/python3
 
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明，使这里的num为全局变量
    print(num) 
    num = 123
    print(num)

fun1()
print(num)