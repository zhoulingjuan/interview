'''
描述
写出一个程序，接受一个正浮点数值，输出该数值的近似整数值。如果小数点后数值大于等于 0.5 ,向上取整；小于 0.5 ，则向下取整。
数据范围：保证输入的数字在 32 位浮点数范围内
'''
import sys

print("请输入一个正浮点数：")
num = sys.stdin.readline()
x, y = num.split('.')
if int(y) >= 5:
    print(int(x)+1)
else:
    print(int(x))
