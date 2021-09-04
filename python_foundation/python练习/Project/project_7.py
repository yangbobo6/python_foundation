#练习7
# 打印二维数组，值位每行*每列
list = [int(i) for i in input().split(',')]  #列表推导式
x = list[0]
y = list[1]
#  x,y = map(int,input().split(','))  map代替上面的输入  map函数  映射
#  lst = [[i*j for j in range(y)] for i in range(x)]  列表推导式
list2 = []
for i in range(0,x+1):
    list1 = []
    for j in range(0,y+1):
        list1.append(i*j)
    list2.append(list1)
print(list2)

#练习8
#编写一个程序，该程序接受以逗号分隔的单词序列作为输入，并在按字母顺序对单词进行排序后以逗号分隔的顺序打印这些单词。
#假设将以下输入提供给程序：  without,hello,bag,world  输出：bag,hello,without,world
list_string = input().split(",")
list_string.sort()
print(list_string)
print(','.join(list_string))

#练习9  编写一个接受行序列作为输入的程序，并在使句子中的所有字符都大写之后打印行。
#假设将以下输入提供给程序：
#Hello world
#Practice makes perfect
#主要练习怎样换行输入 1）
list_upper = []
while True:
    x = input()
    if len(x) == 0:  #输入第二次回车就是0
        break
    list_upper.append(x.upper())
for line in list_upper:
    print(line)

#方法 2）  生成器
def print_upper():
    while True:
        s = input()
        if not s:   #输出判断
            return
        yield s   #
for line in map(str.upper,print_upper()):
    print(line)

#问题10  编写一个程序，该程序接受一系列由空格分隔的单词作为输入，并在删除所有重复的单词并将其按字母数字顺序排序后打印这些单词。
# 假设将以下输入提供给程序：hello world and practice makes perfect and hello world again
#结果：again and hello makes perfect practice world
list_10 = input().split()
list_10_set = [str(i) for i in set(list_10)]
list_10_set.sort()
print(' '.join(list_10_set))

#编写一个程序，该程序接受以逗号分隔的4位二进制数字序列作为输入，然后检查它们是否可被5整除。被5整除的数字将以逗号分隔的顺序打印。
#例子：  0100,0011,1010,1001   输出1010
def check(x):
    total = 0
    pw = 1
    reversed(x)
    #二进制转化为十进制
    for i in x:
        total = total+pw*(ord(i)-48)  #ascii 符号，转化为十进制  ord(0) 是48
        print(i)
        pw*=2
    return total%5

binary_list = input().split(',')
lst = []
for i in binary_list:
    if check(i)==0:
        lst.append(i)
print(','.join(lst))

#解法2)
data = input().split(',')
data = [num for num in data if int(num, 2) % 5 == 0]
print(','.join(data))


