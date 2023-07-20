# coding:utf-8
# I am learning python
# time:2022/12/17 20:05

"""
字典的标志：两边两个大括号
元素由键、值组成，格式为 键:值  以逗号隔开
键、值都可以是任何数据类型
通过 字典变量名[键] 取出键对应的值
"""

dict1 = {
    114: 514,
    '1919': 810,
    '会唱': True,
    '会跳': True,
    '会rap': True,
    '会打篮球': True,
    '你干嘛': '黑子',
        }
a = dict1[114]
print(a, type(a))

b = dict1['1919']
print(b, type(b))

c = dict1['你干嘛']
print(c, type(c))

d = dict1['会跳']
print(d, type(d))

if dict1['会唱'] and dict1['会跳'] and dict1['会rap'] and dict1['会打篮球']:
    print('没错了，你就是坤坤！')


#字典的遍历
dict2 = {
    '迷你世界': '垃圾盗版',
    'MineCraft': 'nb正版',
    'pi': 3.14159265358979323846,
    114514: 1919810
}
for i in dict2:
    print(i, end=',')   #遍历字典遍历出的是键
    print(dict2[i])    #可以用键取值


#字典值的修改与新建

#修改:
#使用 列表名[键] = 值
dict2['pi'] = 3.14
print(dict2)

#新建：
#使用 列表名[列表中不存在的键] = 值
dict2['e'] = 2.71828
print(dict2)








