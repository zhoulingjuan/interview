import sys
'''
描述
计算字符串最后一个单词的长度，单词以空格隔开，字符串长度小于5000。（注：字符串末尾不以空格为结尾）
输入描述：
输入一行，代表要计算的字符串，非空，长度小于5000。

输出描述：
输出一个整数，表示输入字符串最后一个单词的长度。
'''

while True:
    print("请输入：")
    line = sys.stdin.readline().strip()
    print(line)
    if line == '':
        print("输入为空")
        break
    lines = line.split() ##默认是按空格分割
    print(lines[-1]+"字符个数为：") ##列表-1取最后一个元素
    print(len(lines[-1]))  ##内置函数len()直接得到结果