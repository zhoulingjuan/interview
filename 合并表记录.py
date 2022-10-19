'''
描述
数据表记录包含表索引index和数值value（int范围的正整数），请对表索引相同的记录进行合并，
即将相同索引的数值进行求和运算，输出按照index值升序进行输出。
'''
import sys

print("请输入键值对的个数：")
number = int(sys.stdin.readline().strip())
i = 1
dic = {}
print("请输入键值对，空格分开：")
while i <= number:
    line = sys.stdin.readline().strip()
    k = line.split()[0]
    v = line.split()[1]
    dic[k] = dic.get(k, 0) + int(v) ##注意！！这里就可以累加了！即使字典没有key和value，也不会报错！
    i = i+1  ##计数器别忘记加上！

print("输出结果为：")
##排序注意一下，不能一部到位，for循环一下
for each in sorted(dic):
    print(each, dic[each])