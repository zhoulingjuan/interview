'''
以上三角形的数阵，第一行只有一个数1，以下每行的每个数，是恰好是它上面的数、左上角数和右上角的数，3个数之和（如果不存在某个数，认为该数就是0）。
求第n行第一个偶数出现的位置。如果没有偶数，则输出-1。例如输入3,则输出2，输入4则输出
'''
import sys

print("请输入行数：")
n = int(sys.stdin.readline().strip())

if n == 1 or n == 2:
    print(-1)
elif (n + 1) % 2 == 0:
    print(2)
elif n % 4 == 0:
    print(3)
elif (n + 2) % 4 == 0:
    print(4)




