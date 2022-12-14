'''
输出 1到n之间 的与 7 有关数字的个数。
一个数与7有关是指这个数是 7 的倍数，或者是包含 7 的数字（如 17 ，27 ，37 ... 70 ，71 ，72 ，73...）
'''

'''
1、&&和||分别为短路与和短路或
&&若前面的表达式结果为false，整个逻辑表达式的结果就为false，所以后面的表达式无论true或者false都无法影响整个逻辑表达式的结果，
所以为了提高代码执行效率，后面的表达式就不会执行。
同理，若前面的表达式为true，则后面的表达式也无需计算。
2、&和|为不短路与和不短路或
无论什么情况,前面的和后面的表达式都要执行。
'''

n = input("请输入n:").strip()
result = []

for i in range(1, int(n)+1):
    print(i)
    if str(i).__contains__('7') or i % 7 == 0:  ##或用的是or，不是|
        print(i)
        result.append(i)
print(result)
