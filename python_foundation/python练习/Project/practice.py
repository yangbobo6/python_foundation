def check(x):
    total = 0
    pw = 1
    reversed(x)
    #二进制转化为十进制
    print(type(x))
    for i in x:
        total = total+pw*(ord(i)-48)
        print(i)
        pw*=2
    return total%5

binary_list = input().split(',')
lst = []
for i in binary_list:
    if check(i)==0:
        lst.append(i)
print(','.join(lst))

