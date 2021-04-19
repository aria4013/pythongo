#如果你需要遍历数字序列，可以使用内置range()函数。它会生成数列
for i in range(5):
    print(i)

#你也可以使用range指定区间的值：
for i in range(5,9) :
    print(i)

#也可以使range以指定数字开始并指定不同的增量(甚至可以是负数，有时这也叫做'步长'):
for i in range(0, 10, 3) :
    print(i)

#负数：
for i in range(-10, -100, -30) :
    print(i)

#您可以结合range()和len()函数以遍历一个序列的索引,如下所示:
a = ['Google', 'Baidu', 'Runoob', 'Taobao', 'QQ']
for i in range(len(a)):
    print(i, a[i])

#还可以使用range()函数来创建一个列表：
list(range(5))