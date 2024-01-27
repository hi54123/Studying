# coding:utf-8
# I am learning python
# time:2023/1/26 20:17

"""
try语句最完整的状态为：
try:
    ...

except ... :
    ...

except ... :
    ...

...

else:
    ...

finally:
    ...

当try语句有错误时
查看except有无捕捉到错误
如果没有，则报错并执行finally语句中的语句块

没有错误时
执行else与finally中的语句块

else与finally非必要
finally除非解释器停止运行，否则无论如何一定会执行
"""

print('例1，无错误')
try:
    int('123')

except ValueError:
    print('ValueError')

else:
    print('else')

finally:
    print('finally')

print('\n\n例2，有错误，捕捉成功')
try:
    int('awa')

except ValueError:
    print('ValueError')

else:
    print('else')

finally:
    print('finally')


"""print('\n\n例4，遇见quit()')
try:
    int('1')
    quit()
    
except ValueError:
    print('ValueError')

else:
    print('else')

finally:
    print('finally')"""
#结果：finally


print('\n\n例5，遭遇return')


def func():
    try:
        int('1')
        return None

    except ValueError:
        print('ValueError')

    else:
        print('else')

    finally:
        print('finally')


func()


print('\n\n例6，遭遇break/continue')
for _ in range(2):
    try:
        int('1')
        continue

    except ValueError:
        print('ValueError')

    else:
        print('else')

    finally:
        print('finally')

while True:
    try:
        int('awa')

    except ValueError:
        print('ValueError')
        break
    else:
        print('else')

    finally:
        print('finally')


print('\n\n例3，有错误，捕捉失败')
try:
    int('awa')

except AttributeError:  # 随便写的，因为它在第一个
    print('AttributeError')

else:
    print('else')

finally:
    print('finally')
