# 方法1
test_str = "Runoob"
new_str = test_str.replace(test_str[3], "", 1)
print(new_str)

# 方法2
str = 'Runoob'

'''
@param str 原字符串
@paramnum 要移除的位置
@return 移除后的字符串
'''

def ff(str,num):
    return str[:num] + str[num+1:];
print(ff(str,2));
print(ff(str,4));