# coding:utf-8
# I am learning python
# time:2022/12/31 21:06

"""
while-else语句:
当while的条件不成立时
执行else内部语句

简单来说：
while正常结束执行else
遭遇break不执行else
"""
#始终不成立
while False:
    print('false')
else:
    print('else 1')

print('___________________________________')
#开始成立，接着不成立
a = 0
while a < 5:
    print(a)
    a += 1
else:
    print('else 2')

print('--------------------------------------------------')

#遭遇break
while True:
    print('break')
    break
else:
    print('else 3')