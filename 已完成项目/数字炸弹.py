# coding:utf-8
# I am learning python
# time:2022/12/29 18:04

from random import randint
import time


print('Hello')
print("这是一个数字炸弹游戏")
print("""
    规则如下：
        计算机会生成一个数字作为“数字炸弹”
        然后你和计算机会轮流猜一个数
        根据你们的数缩小范围
        猜到“数字炸弹”的就输了
        """)
_ = input('回车以继续...')
print('游戏开始')
time.sleep(0.5)
r = 0

while True:
    print('生成“数字炸弹”中')
    bomb = randint(0, 101)
    time.sleep(0.75)
    print('生成完成，可以开始游戏')
    start = 0
    end = 100

    while True:
        r += 1
        print(f'回合{r}')

        while True:
            player_ans = input(f'请输入一个{start}~{end}以内的正整数')
            if player_ans.isdecimal():
                player_ans = int(player_ans)
                if start < player_ans < end:

                    if player_ans > bomb:
                        end = player_ans
                        print(f'你猜大了。\n{start}~{end}\n')

                    elif player_ans < bomb:
                        start = player_ans
                        print(f'你猜小了。\n{start}~{end}\n')

                    if player_ans == bomb:
                        print(f'BOOM!炸弹是{bomb}')
                        print(' 你 踩到了炸弹，你输了:(')
                        break

                    computer_ans = randint(start, end)
                    if computer_ans > bomb:
                        end = computer_ans
                        print(f'电脑选择了{computer_ans}猜大了。\n{start}~{end}\n')
                    elif computer_ans < bomb:
                        start = computer_ans
                        print(f'电脑选择了{computer_ans}猜小了。\n{start}~{end}\n')

                    if computer_ans == bomb:
                        print(f'BOOM!!!!!!!!!!\n炸弹是{bomb}')
                        print(r' 电脑 踩到了炸弹，你赢了 \(^_^)/')
                        break

                else:
                    print('输入数值过大、过小，或非整数。请重新输入')
                    continue

            else:
                print('输入数值过大、过小，或非整数。请重新输入')
                continue

        op = input('再来一局？(y/n)')
        if op == 'y':
            continue
        else:
            quit(0)
