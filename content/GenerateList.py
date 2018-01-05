#import os

#         for循环
# a = [a + b + d for b in 'abc' for a in 'zxc' for d in 'qwe' if a + b + d == 'cce']
# print (a)
#d = [d for d in os.listdir('.')]
#print (d)


#         迭代字典
# a = {'x':'X','s':'S','a':'A'}
# for x , y in a.items():
#     print (x,'=',y)
# print ('key is',a.keys(),'value is',a.values(),'item is',a.items())


#         isinstance 判断类型

 # x = '123'
 # y = 123
 # isinstance(x, str)

 #           generator生成器
 #a = (for x in range(10))
 #generator和list的区别在括号不同

 #     interator迭代器
 # b = iter([1,2,3,4])
 # while True:
 #     try:
 #         c = next(b)
 #     except StopIteration:
 #         break

 #        高阶函数
def add(a,b,c):
    return c(a) + c(b)
print(add(-5, -10, abs))

