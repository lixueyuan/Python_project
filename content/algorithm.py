def fact(n):
    if n == 1:
        return 1
    return n * fact(n - 1)
a = int(input('输入一个数字'))
print ('乘积为',fact(a))
