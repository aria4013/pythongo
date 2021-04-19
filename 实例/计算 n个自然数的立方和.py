# 方法1

n = int(input("请输入正整数n: "))

sum = 0
for i in range(1, n+1, 1):
    sum = sum + i**3
print(sum)

# 方法2

# 使用递归函数来计算 n 个自然数之和：

def sum_up(n:int) -> int:
    if n <= 1:
        return n
    else:
        return sum_up(n-1) + n**3

number = int(input("请输入一个自然数: ").strip())
print(sum_up(number))