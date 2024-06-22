# coding:utf-8
# I am learning python
# time:2022/12/29 18:03

from random import randint
from time import sleep

print('Hello!')
print("""
        这是一个猜数字的小游戏
        计算机会从你给定的范围里生成一个数字
        你需要猜出这个数字
        每回答一个数字，电脑都会告诉你你猜大了还是小了
        接下来，开始吧！
        """)
_ = input('回车以继续...')
while True:
    print('请选择模式：')
    op = input('1:无限次数, 2:规定次数。退出请按q\n')

    # 无限次数
    if op == '1':
        while True:
            ran = input('请输入数字取值的范围, 0~')
            if ran.isdecimal():
                ran = int(ran)
                num = randint(0, ran + 1)
                times = 0
                sleep(0.75)
                print('生成完成，开始猜吧')

                while True:
                    ans = input('输入数字')
                    if ans.isdecimal():
                        ans = int(ans)
                        times += 1
                        if ans > num:
                            print('你他妈的猜得太大了')

                        elif ans < num:
                            print('你猜得真他妈的小')

                        elif ans == num:
                            if times == 1:
                                print('这么有实力？！一发入魂')
                                break
                            print(f'恭喜你他娘的猜对了。一共用了{times}次')

                    else:
                        print('你输的什么鬼东西，给老子输入整数')

                op2 = input('此模式再来一局？退出将回到模式选择(y/n)')
                if op2 == 'y':
                    continue

                else:
                    break

            else:
                print('你他妈输的什么鬼东西，给老子输入整数')

    # 规定次数
    elif op == '2':
        while True:
            ran = input('请输入数字取值的范围, 0~')
            if ran.isdecimal():
                ran = int(ran)
                num = randint(0, ran + 1)
                can_Times = input('你觉得你能几次猜对\n')
                times = 0
                if can_Times.isdecimal():
                    can_Times = int(can_Times)
                    sleep(0.75)
                    print('生成完成，开始猜吧')
                    while True:
                        ans = input('输入数字')
                        if ans.isdecimal():
                            ans = int(ans)
                            times += 1

                            if ans > num:
                                print(f'你他妈的猜得太大了，还剩{can_Times - times}次机会，给爷好好珍惜吧')

                            elif ans < num:
                                print(f'你猜得真他妈的小，还剩{can_Times - times}次机会，给爷好好珍惜吧')

                            elif ans == num:
                                if times == 1:
                                    print('这么有实力？！一发入魂')
                                    break
                                print(f'恭喜你他娘的猜对了。一共用了{times}次')

                        else:
                            print('你他妈输的什么鬼东西，给老子输入整数')

                    op2 = input('此模式再来一局？退出将回到模式选择(y/...)')
                    if op2 == 'y':
                        continue

                    else:
                        break

                else:
                    print('你他妈输的什么鬼东西，给老子输入整数')
            else:
                print('你他妈输的什么鬼东西，给老子输入整数')

    elif op == 'q':
        quit(0)

    else:
        print('你他妈输的什么鬼东西，给老子输入整数')
