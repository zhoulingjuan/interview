'''
描述
•输入一个字符串，请按长度为8拆分每个输入字符串并进行输出；

•长度不是8整数倍的字符串请在后面补数字0，空字符串不处理。
输入描述：
连续输入字符串(每个字符串长度小于等于100)

输出描述：
依次输出所有分割后的长度为8的新字符串
'''

import sys

def f(str, num, list=[]):
    if len(str) <=num:
        list.append(str.strip()+"0"*(num-len(str.strip()))) ##注意！！！str.strip()先去除换行符
        return list
    else:
        list.append(str[:num])
        return f(str[num:], num, list)  ##用递归！！！

if __name__ == '__main__':
    print("请输入长度小于100的字符串：")
    str = sys.stdin.readline()
    print(f(str, 8))
