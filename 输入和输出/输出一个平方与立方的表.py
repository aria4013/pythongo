for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # 注意前一行 'end' 的使用
    print(repr(x*x*x).rjust(4))

for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))

# 注意：在第一个例子中, 每列间的空格由 print() 添加。

# 这个例子展示了字符串对象的 rjust() 方法, 它可以将字符串靠右, 并在左边填充空格。

# 还有类似的方法, 如 ljust() 和 center()。 这些方法并不会写任何东西, 它们仅仅返回新的字符串。

# 另一个方法 zfill(), 它会在数字的左边填充 0，如下所示：

print('12'.zfill(5))
print('-3.14'.zfill(7))
print('3.14159265359'.zfill(5))
