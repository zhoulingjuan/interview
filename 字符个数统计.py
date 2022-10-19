'''
描述
编写一个函数，计算字符串中含有的不同字符的个数。字符在 ASCII 码范围内( 0~127 ，包括 0 和 127 )，换行表示结束符，不算在字符里。不在范围内的不作统计。多个相同的字符只计算一次
例如，对于字符串 abaca 而言，有 a、b、c 三种不同的字符，因此输出 3 。
'''

str = input("请输入字符串：").strip()
list0 = set(list(str))  ##利用set()方法去重
str0 = ''.join(list0)
k = 0;
for i in str0:
    if ord(i)>=1 & ord(i) <=127:
        k = k+1
print(k)