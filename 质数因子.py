'''
描述
功能:输入一个正整数，按照从小到大的顺序输出它的所有质因子（重复的也要列举）（如180的质因子为2 2 3 3 5 ）
数据范围： 大于等于1
'''
import sys

'''若一整数能除尽另一整数，则前者称为后者的因数。比如8的因数有1，2,4,8。但8的质因子只有2'''

def get_num_factors(num):
    list0 = []
    tmp = 2
    while (num >= tmp):
        k = num % tmp ##余数为0
        if (k == 0):
            list0.append(tmp)
            num = num / tmp  # 更新
        else:
            tmp = tmp + 1  # 同时更新除数值，不必每次都从头开始
    return list0

if __name__ == '__main__':
    print("请输入一个正整数：")
    num = int(sys.stdin.readline().strip())
    if num == 1:
        print("1 没有质因子！")
    else:
        print("所有质因子，从小到大为：")
        print(get_num_factors(num))


