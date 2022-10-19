import sys
'''
描述
明明生成了NN个1到500之间的随机整数。请你删去其中重复的数字，即相同的数字只保留一个，把其余相同的数去掉，然后再把这些数从小到大排序，按照排好的顺序输出。

数据范围： 1 \le n \le 1000 \1≤n≤1000  ，输入的数字大小满足 1 \le val \le 500 \1≤val≤500 
输入描述：
第一行先输入随机整数的个数 N 。 接下来的 N 行每行输入一个整数，代表明明生成的随机数。 具体格式可以参考下面的"示例"。
输出描述：
输出多行，表示输入数据处理后的结果
'''
while True:
    print("请输入1~1000之间的整数：")
    str = sys.stdin.readline().strip()
    if str.isdigit(): ## isdigit() 方法检测字符串是否只由数字组成，只对 0 和 正数有效。
        i = 1;
        num_list = [];
        while i <= int(str):  ##用int()方法转换为整数
            print("请输入单个数字：")
            single_num = sys.stdin.readline().strip()
            if single_num.isdigit():
                num_list.append(single_num)
            else:
                print("请重新输入正确的整数：")
            i = i+1;
        print("排序结果为：")
        print(num_list.sort())  ##排序规则，reverse = True 降序， reverse = False 升序（默认），无返回值！
        print(num_list)
        '''
        注意！！！sort是在原位重新排列列表，无返回值，而sorted()是产生一个新的列表，有返回值
        sort 是应用在 list 上的方法，sorted 可以对所有可迭代的对象进行排序操作
        '''
        break
    else:
        print("请重新输入1~1000之间的整数：")



