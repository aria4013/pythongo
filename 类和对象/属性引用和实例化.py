# 属性引用使用和 Python 中所有的属性引用一样的标准语法：obj.name。

# 类对象创建后，类命名空间中所有的命名都是有效属性名。所以如果类定义是这样:

#!/usr/bin/python3
 
class MyClass:
    """一个简单的类实例"""
    i = 12345
    def f(self):
        return 'hello world'
 
# 实例化类
x = MyClass()
 
# 访问类的属性和方法
print("MyClass 类的属性 i 为：", x.i)
print("MyClass 类的方法 f 输出为：", x.f())