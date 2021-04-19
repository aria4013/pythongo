# 方法1
list=[1,3,5,7,9,34]
sum=0
for i in range(0,len(list)):
    sum+=list[i]
print(sum)

# 方法2
from functools import reduce
list=[1,3,5,7,9,34]

print(reduce(lambda x,y:x+y,list))