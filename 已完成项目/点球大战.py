# coding:utf-8
# I am learning python
# time:2022/12/27 14:24
from random import choice


player_id = input('请输入你的玩家名:')

print(f'{player_id}你好，欢迎来到点球大战，游戏即将开始，请做好准备')
input('回车以继续......\n')

print('游戏开始！\n')

print("""游戏规则：
你需要选择一个射门方向，机器也会随机选择射门方向
如果方向不同，你就赢了。
如果方向相同你就输了
简单吧，简单就开始吧！
""")
input('回车以开始\n\n')

print('请选择射门方向')
# 初始化变量
way = ['left', 'middle', 'right']
player_score = 0
computer_score = 0
times = 5
computer_times = 5
# 输入方向

q = 3
while True:
    player_choose = input(way)

    if player_choose in way:
        computer_choose = choice(way)
        # 计算胜负

        if player_choose == computer_choose:
            computer_score += 1
            times -= 1
            print('噢，真不幸,你的球被拦住了')
            print(f'比分：{player_score}:{computer_score}\n')

        if player_choose != computer_choose:
            player_score += 1
            times -= 1
            print("GOAL! 你的球进了")
            print(f"比分：{player_score}:{computer_score}\n")

        if player_score + times < computer_score:
            print(f'你输了\n比分：{player_score}:{computer_score}')
            quit()

        if computer_score + times < player_score:
            print(f'你赢了\n比分：{player_score}:{computer_score}')
            quit()

        if times <= 0:
            break

    else:
        q -= 1
        if q > 0:
            print(f'输入错误，请重新输入。再次错误{q}次便会退出游戏')
            continue
        else:
            print('错误次数已用尽，退出游戏')
            quit()

if computer_score > player_score:
    print(f'很遗憾，你输了\n比分：{player_score}:{computer_score}')
else:
    print(f'呜呼~~~你赢了\n比分：{player_score}:{computer_score}')
