'''
给定一个字符串描述的算术表达式，计算出结果值。
输入字符串长度不超过 100 ，合法的字符包括 ”+, -, *, /, (, )” ， ”0-9” 。
'''

'''
pow() 方法返回 xy（x 的 y 次方） 的值。
eval() 函数用来执行一个字符串表达式，并返回表达式的值。
'''
s = input("请输入算术表达式：").strip()

print(eval(s))

