# coding:utf-8
# I am learning python
# time:2022/11/20 15:49


"""
用 % 对字符串进行格式化
"""

#   %d 用于格式化 整数 或 整数变量
num = 18
print('My age is %d' % num)  # My age is 18

#   %f 用于格式化 浮点数 或 浮点数变量，默认小数点后6位
print('float is %f' % 4.99)  # float is 4.990000
#   若要规定精确位数，使用%.[位数]f  如4.99使用%.2f
print('float is %.2f' % 4.99)  # float is 4.99

#   %s 用于格式化 字符串 或 字符串变量
adj = 'interesting'
print('Minecraft is %s.' % adj)

#   %也可以格式化多个量
n = 'game'
adj = 'interesting'
print("Minecraft is a good %s and it's so %s." % (n, adj))
# 注意：变量与%要一一对应，类型也要一一对应
print("-------------------------------------------------------------------------------------------------------")
print("-------------------------------------------------------------------------------------------------------")
'''
用fString 或 {}与.format
'''

# 使用f String (python3.6+)
name = '蔡徐坤'
age = 114514
hobby = ("唱", "跳", "rap", "篮球")
print(f'全民制作人们大家好，我是练习时长两年半的个人练习生{name}，喜欢{hobby}。music~')
print(f'你干嘛~我才活了{age}岁')

# 使用{}与.format
name = '蔡徐坤'
age = 114514
hobby = ("唱", "跳", "rap", "篮球")
print('全民制作人们大家好，我是练习时长两年半的个人练习生{}，喜欢{}。music~'.format(name, hobby))
print('你干嘛~我才活了{}岁'.format(age))

# .format 2
text = "这里是空格1-->|{0}|<--空格1。这里是空格2-->|{1}|<--空格2".format("awa", "qwq")
print(text)

# .format 3
text2 = "重复空格1 -->|{0}|<-- 。普通空格-->|{1}|。重复空格1 -->|{0}|<--使用相同数字标识".format("awa", "qwq")
print(text2)

# .format 4
text3 = "全体目光向我看齐，看我看我，我宣布个事儿。我是{sb}".format(sb="傻逼")
print(text3)
text4 = "{idol}为我下蛋，给我吃，真的太{adj}了".format(idol="坤坤", adj="伟大")
print(text4)
