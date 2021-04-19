a = [66.25, 333, 333, 1, 1234.5]
#count返回 x 在列表中出现的次数
print(a.count(333), a.count(66.25), a.count('x'))
#insert在指定位置插入一个元素。第一个参数是准备插入到其前面的那个元素的索引，例如 a.insert(0, x) 会插入到整个列表之前，而 a.insert(len(a), x) 相当于 a.append(x) 。
a.insert(2, -1)
#append把一个元素添加到列表的结尾，相当于 a[len(a):] = [x]。
a.append(333)
print(a)
#index返回列表中第一个值为 x 的元素的索引。如果没有匹配的元素就会返回一个错误。
a.index(333)
#remove删除列表中值为 x 的第一个元素。如果没有这样的元素，就会返回一个错误。
a.remove(333)
print(a)
#reverse从后往前重新排列列表中的元素。
a.reverse()
print(a)
#sort对列表中的元素进行排序。
a.sort()
print(a)
