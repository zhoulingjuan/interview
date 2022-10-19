'''
描述
写出一个程序，接受一个十六进制的数，输出该数值的十进制表示。

数据范围：保证结果在 1<= n <=2^31−1

输入描述：
输入一个十六进制的数值字符串。

输出描述：
输出该数值的十进制字符串。不同组的测试用例用\n隔开。
'''
import sys

'''
二进制前缀为0b，八进制前缀为0o，十六进制前缀为0x 
'''

if __name__ == '__main__':
    '''
    二进制转十进制：int("1010",2)
    八进制转十进制：int("0o12",8)
    十六进制转十进制：int("0xa",16)
    '''
    print("请输入十六进制的数：")
    num = sys.stdin.readline()
    #十六转十
    print(int(num, 16))

    '''
    十进制转二进制：bin(num)
    十进制转八进制：oct(num)
    十进制转十六进制：hex(num)
    '''
    #十进制转二进制
    print(bin(int(num)))  ##先将字符串用int()方法转换成十进制
    #十进制转八制
    print(oct(int(num)))
    #十进制转十六进制
    print(hex(int(num)))

    '''
    需要十进制中转的进制转换：
    二转八：二转十，再转八——oct(int("1010",2))
    八转十六：八转十，再转十六——hex(int("12",8))
    '''


