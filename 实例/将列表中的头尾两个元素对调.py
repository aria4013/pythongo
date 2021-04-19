arr = list(map(int,input("请输入数组：").split()))
arr.insert(0,arr.pop())
arr.append(arr.pop(1))
print(arr)