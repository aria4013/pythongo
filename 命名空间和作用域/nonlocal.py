#!/usr/bin/python3
 
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明，num非局部变量
        num = 100
        print(num)
    inner()
    print(num)


outer()