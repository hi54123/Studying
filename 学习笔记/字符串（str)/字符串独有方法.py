# coding:utf-8
# I am learning python
# time:2023/1/2 13:27

#判断字符串是否由...开头
v1 = '我是你爸爸'
if v1.startswith('我'):
    print('是由“我”开头')
else:
    print('不是由“我”开头')

#判断字符串是否由...结尾
if v1.endswith('爸爸'):
    print('是由“爸爸”结尾')
else:
    print('是由“爸爸”结尾')

#判断是否完全为整数
v2 = '114514'
if v2.isdecimal():
    print('它是整数,可以int()')

#字符串去两边空白/指定字符
v3 = "   114514 1919 810   "
print('|' + v3.strip() + '|')  #去两边空白
print('|' + v3.rstrip() + '|')  #去除右边空白
print('|' + v3.lstrip() + '|')  #去除左边空白

v4 = '1我是一行测试的字符1'
print(v4.strip('1'))  #去两边字符
print(v4.rstrip('1'))  #去右边字符
print(v4.lstrip('1'))  #去左边字符


#字符串变大写
v5 = 'minecraft'
print(v5.upper())

#字符串变小写
v6 = 'MineCraft'
print(v6.lower())
