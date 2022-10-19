'''
描述
正整数A和正整数B 的最小公倍数是指 能被A和B整除的最小的正整数值，设计一个算法，求输入A和B的最小公倍数。
'''



def lcm(x, y):
    #  获取最大的数
    if x > y:
        greater = x
    else:
        greater = y

    while True:
        if ((greater % x == 0) and (greater % y == 0)):
            break
        greater += 1

    return greater

if __name__ == '__main__':
    line = input("请输入整数A和B，用空格隔开：").strip()
    print(line)
    A = int(line.split()[0])
    B = int(line.split()[1])
    N = lcm(A, B)
    print("最小公倍数为：" + str(N))