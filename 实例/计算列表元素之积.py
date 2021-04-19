# 方法1
def multiplyList(myList) :
     
    result = 1
    for x in myList:
         result = result * x  
    return result  
     
list1 = [1, 2, 3]  
list2 = [3, 2, 4]
print(multiplyList(list1))
print(multiplyList(list2))

# 方法2
from functools import reduce
list1 = [1,3,5,6,7]
sum = reduce(lambda x,y:x*y,list1)
print(sum)

# 方法3
# 采用递归方法：

def list_product(list_1,size):
    if size == 0:
        return 1    
    else:
        return list_1[size-1] * list_product(list_1,size - 1)


list_1 = [i for i in range(3,6)] #生成列表[3,4,5]
print(list_1)
print(list_product(list_1,len(list_1)))