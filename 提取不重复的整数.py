'''
描述
输入一个 int 型整数，按照从右向左的阅读顺序，返回一个不含重复数字的新的整数。
保证输入的整数最后一位不是 0 。
'''

num = input("请输入整数：").strip().strip('0') ##移除最后的字符0
num2 = ''.join(reversed(num))  ##先将字符串逆序
print(num2)
dic = {}
for i in num2:
    dic[i]=''

num3 = ''.join(dic.keys())  ##join将列表转化为字符串
print(int(num3))