
#1.编写一个程序，查找所有此类数字，它们可以被7整除，但不能是5的倍数（在2000和3200之间（均包括在内））。获得的数字应以逗号分隔的顺序打印在一行上。
from functools import reduce

l = []
for i in range(2000,3201):
    if i%7==0 and i%5!=0:
        l.append(str(i))

print(','.join(l))
#使用生成器和列表打印
print(*(i for i in range(2000,3201) if i%7==0 and i%5!=0),sep=',')

#2.编写一个程序，可以计算给定数字的阶乘，结果应以逗号分隔的顺序打印在一行上，假设向程序提供了以下输入：
# 8然后，输出应为：40320
#1)循环解决
i = int(input())
plus = i
while i != 1:
    i = i-1
    plus = plus*i
print(plus)

#2)递归
i = int(input())
def plus(n):
    if n<=1:
        return 1
    return n*plus(n-1)
print(plus(i))

#3)reduce函数
def f(acc,item):
    return acc*item
num = int(input())
print(reduce(f,range(1,num+1),1)) #后面的1保证从1开始

#3.使用给定的整数n，编写程序以生成包含（i，ixi）的字典，
# 该字典为1到n之间的整数（都包括在内）。然后程序应打印字典。
# 假设向程序提供了以下输入：8\然后，输出应为：{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
#)1for循环
i = int(input())
d = {}
for i in range(1,i+1):
    d[i] = i*i
print(d)
#2) 字典
n = int(input())
d = {i:i*i for i in range(1,n+1)}
print(d)
#3)
num = int(input("Number: "))
print(dict(enumerate([i*i for i in range(1, num+1)], 1)))

#问题4:编写一个程序，该程序从控制台接受一个逗号分隔的数字序列，
# 并生成一个列表和一个包含每个数字的元组。假设向该程序提供了以下输入：
#34,67,55,33,12,98
lst = input().split(',')  #list 列表
tup = tuple(lst)  #元组

#问题5：定义一个至少具有两个方法的类：
# getString：从控制台输入获取字符串
# printString：以大写字母打印字符串   还请包括简单的测试功能来测试类方法。
class IOstring():
    def getString(self):
        self.s = input()

    def printString(self):
        print(self.s.upper())
iostring = IOstring()
iostring.getString()
iostring.printString()

#问题6编写一个程序，根据给定的公式计算并打印该值：
# Q = [(2 * C * D)/ H]的平方根
# 以下是C和H的固定值：
# C为50。H为30。
# D是变量，其值应以逗号分隔的顺序输入到您的程序中，例如，让我们假设以下逗号分隔的输入顺序被赋予了程序：
#100,150,180   输出18,22,24
from math import sqrt;
C,H = 50,30
def calc(D):
    D = int(D)
    return str(int(sqrt((2*C*D)/H)))
D = input().split(',')
D = list(map(calc,D))    #在D上应用calc函数并存储为列表
print(",".join(D))

#2)
from math import sqrt  #导入特定功能，因为使用*导入所有功能
                      #是不好的做法
C,H = 50,30
def calc(D):
    return sqrt((2*C*D)/H)

D = [int(i) for i in input().split(',')]# 在逗号位置＃分裂和在列表中设置
D = [int(i) for i in D]    #转换字符串整数
D = [calc(i) for i in D]  # 返回浮点值通过在d每个项目计算方法
D = [round(i) for i in D]# 所有的浮动值是圆形的
D = [str(i) for i in D]   # 所有整数被转换成字符串，以便能够应用加入操作

print(",".join(D))

#3) 方法
from math import sqrt
C,H = 50,30

def calc(D):
    return sqrt((2*C*D)/H)
D = input().split(',')                    # 在逗号位置＃分裂和设置在列表中
#从里往外   int转化为整数  calc计算   round约等于  str转化成字符串
D = [str(round(calc(int(i)))) for i in D]  # 使用理解方法＃。
print(type(D))
print(",".join(D))
