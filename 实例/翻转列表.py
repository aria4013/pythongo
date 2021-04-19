# 还可以直接调用 list 列表的 sort 方法, 设置 reverse 为 True 即可翻转列表：

li = [*range(10, 16)]
# 得到列表 li = [10, 11, 12, 13, 14, 15], * 为解包符号
print(li)

# 降序排列
li.sort(reverse = True)
print(li)
# 输出: [15, 14, 13, 12, 11, 10]