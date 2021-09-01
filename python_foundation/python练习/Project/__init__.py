from math import sqrt  #导入特定功能，因为使用*导入所有功能
                      #是不好的做法
C,H = 50,30
def calc(D):
    return sqrt((2*C*D)/H)

D = [int(i) for i in input().split(',')]# 在逗号位置＃分裂和在列表中设置
print(D,type(D))
D = [int(i) for i in D]    #转换字符串整数
print(D,type(D))
D = [calc(i) for i in D]  # 返回浮点值通过在d每个项目计算方法
print(D,type(D))
D = [round(i) for i in D]# 所有的浮动值是圆形的
print(D,type(D))
D = [str(i) for i in D]   # 所有整数被转换成字符串，以便能够应用加入操作
print(D,type(D))
print(",".join(D))