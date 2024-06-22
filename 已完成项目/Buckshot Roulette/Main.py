import random
import json


class Player1:
	name = ''
	hp = 3
	down = False
	points = 0
	got_items = []
	shots = 0
	hurts = 0
	have_hurts = 0
	knife_used = 0
	beer_used = 0
	glass_used = 0
	handcuff_used = 0
	smoke_used = 0
	phone_used = 0
	epinephrine_used = 0
	changer_used = 0
	medicine_used = 0


class Player2:
	name = ''
	hp = 3
	down = False
	points = 0
	got_items = []
	shots = 0
	hurts = 0
	have_hurts = 0
	knife_used = 0
	beer_used = 0
	glass_used = 0
	handcuff_used = 0
	smoke_used = 0
	phone_used = 0
	epinephrine_used = 0
	changer_used = 0
	medicine_used = 0


class Gun:
	bullets_num = 0
	bullets = []
	damage = 1


class GlobalVariables:
	controller = Player1
	enemy = None
	rounds = 1
	flag = False
	index = 0
	will_change = True
	higest_hp = {1: 3, 2: 4, 3: 6}


def restart():
	Player1.hp = 3
	Player1.points = 0
	Player1.got_items = []
	Player1.shots = 0
	Player1.hurts = 0
	Player1.have_hurts = 0
	Player1.knife_used = 0
	Player1.beer_used = 0
	Player1.glass_used = 0
	Player1.handcuff_used = 0
	Player1.smoke_used = 0

	Player2.hp = 3
	Player2.points = 0
	Player2.got_items = []
	Player2.shots = 0
	Player2.hurts = 0
	Player2.have_hurts = 0
	Player2.knife_used = 0
	Player2.beer_used = 0
	Player2.glass_used = 0
	Player2.handcuff_used = 0
	Player2.smoke_used = 0

	Gun.bullets_num = 0
	Gun.bullets = []
	Gun.damage = 1

	GlobalVariables.controller = Player1
	GlobalVariables.enemy = None
	GlobalVariables.rounds = 1
	GlobalVariables.flag = False
	GlobalVariables.index = 0
	GlobalVariables.will_change = True


def readfile(file):
	with open(file, 'r', encoding='utf-8') as load_f:
		load_dict = json.load(load_f)
	load_f.close()
	return load_dict


def writefile(file, word):
	with open(file, 'w', encoding='utf-8') as f:
		json.dump(word, f, ensure_ascii=False)


def registry():
	name = input("请输入用户名（确认后无法后悔）\n")
	t = 0
	while t < 3:
		t += 1
		password = input("请输入密码（密码为明文输入，请注意偷窥）\n")
		password_again = input("请确认密码（密码为明文输入，请注意偷窥）\n")
		data_dict = readfile('data.json')
		data_list = data_dict["players"]
		for i in data_list:
			if name == i["name"]:
				print('用户已注册，请登录')
				return False
		if password_again == password:
			data_dict["players"].append({
				"name": f"{name}",
				"password": f"{password}",
				"plays": 0,
				"win": 0,
				"lost": 0,
				"shots": 0,
				"hurts": 0,
				"have_hurts": 0,
				"knife_used": 0,
				"beer_used": 0,
				"glass_used": 0,
				"handcuff_used": 0,
				"smoke_used": 0,
				"phone_used": 0,
				"epinephrine_used": 0,
				"changer_used": 0,
				"medicine_used": 0
			})
			writefile("data.json", data_dict)
			print('注册成功！')
			break
		else:
			print('密码不一致，请重新输入')
	else:
		return False
	return True


def login():
	data_dict = readfile('data.json')
	data_list = data_dict["players"]
	print('玩家1登录中')
	t = 0
	while t < 3:
		t += 1
		Player1.name = input("请输入用户名\n")
		password = input("请输入密码（密码为明文输入，请注意偷窥）\n")
		for i in data_list:
			if len(data_list) == 0:
				break
			elif Player1.name == i['name']:
				if password == i['password']:
					GlobalVariables.flag = True
		if GlobalVariables.flag:
			break
		print('用户名或密码错误，请重新输入')
	else:
		return False

	print('玩家2登录中')
	t = 0
	while t < 3:
		t += 1
		Player2.name = input("请输入用户名\n")
		if Player2.name == Player1.name:
			print('\n账号已登录，请勿使用同一个账号\n')
			continue
		password = input("请输入密码（密码为明文输入，请注意偷窥）\n")
		for i in data_list:
			if len(data_list) == 0:
				break
			elif Player2.name == i['name']:
				if password == i['password']:
					return True
		print('用户名或密码错误，请重新输入')
	else:
		return False


def start():
	print("""
Welcome to Buckshot Roulette
""")
	while True:
		op = input("请登录(1)/注册(2)")
		if op == '1':
			res = login()
			if res:
				print('登录成功！')
				return True

			print('登录失败！已退出。')
			return False

		elif op == "2":
			res = registry()
			if not res:
				print('注册失败，已退出')
				return False

		else:
			print('输入错误，请重新输入')


def introduce():
	print("""
	============================================================
	Welcome to Buckshot Roulette！
	欢迎来到《猎枪轮盘》！

	该游戏需要双人进行本地对战，请准备好你的朋友
	（左右互博也不是不可以awa）
	============================================================
	""")
	input("在本行末回车以开始")
	for i in range(20):
		print('\n')


def fight():
	def reload(least, most):
		Gun.bullets_num = random.randint(least, most)
		Gun.bullets = []
		all_true, all_false = True, True
		for i in range(Gun.bullets_num):
			Gun.bullets.append(random.choice([True, False]))
		for i in Gun.bullets:
			if i:
				all_false = False
			else:
				all_true = False

		if all_true or all_false:
			reload(least, most)

		reals, fakes = 0, 0
		for i in Gun.bullets:
			if i:
				reals += 1
			else:
				fakes += 1
		print(f'本回合共有{Gun.bullets_num}颗子弹，实弹{reals}颗，空弹{fakes}颗')

	def shot():
		reload(least, most)
		GlobalVariables.index = 0
		while GlobalVariables.controller.hp > 0 and GlobalVariables.enemy.hp > 0 and GlobalVariables.index < len(
				Gun.bullets):
			op = input(f'现在由 {GlobalVariables.controller.name} 操控枪。1：向对方开枪；2：向自己开枪；3：使用道具\n')
			if op == '1':
				GlobalVariables.controller.shots += 1

				if Gun.bullets[GlobalVariables.index]:
					GlobalVariables.enemy.hp -= Gun.damage
					GlobalVariables.index += 1
					print(
						f'实弹，{GlobalVariables.enemy.name} 扣除{Gun.damage}点血量，剩余 {GlobalVariables.enemy.hp} 点血量\n')
					GlobalVariables.enemy.have_hurts += 1
					GlobalVariables.controller.hurts += 1

					if GlobalVariables.rounds == 3 and GlobalVariables.enemy.down:
						GlobalVariables.enemy.hp = 0

				else:
					print(f'空弹，{GlobalVariables.enemy.name} 未扣除血量，剩余 {GlobalVariables.enemy.hp} 点血量\n')
					GlobalVariables.index += 1

				if GlobalVariables.will_change:
					GlobalVariables.controller, GlobalVariables.enemy = GlobalVariables.enemy, GlobalVariables.controller

				Gun.damage = 1
				GlobalVariables.will_change = True

			elif op == '2':
				GlobalVariables.controller.shots += 1

				if Gun.bullets[GlobalVariables.index]:
					GlobalVariables.controller.hp -= Gun.damage
					GlobalVariables.index += 1
					print(
						f'实弹，{GlobalVariables.controller.name} 扣除{Gun.damage}点血量，剩余 {GlobalVariables.controller.hp} 点血量\n')
					GlobalVariables.controller.have_hurts += 1

					if GlobalVariables.rounds == 3 and GlobalVariables.controller.down:
						GlobalVariables.controller.hp = 0

					if GlobalVariables.will_change:
						GlobalVariables.controller, GlobalVariables.enemy = GlobalVariables.enemy, GlobalVariables.controller
				else:
					print(f'空弹，{GlobalVariables.enemy.name} 未扣除血量，剩余 {GlobalVariables.enemy.hp} 点血量\n')
					GlobalVariables.index += 1

				Gun.damage = 1
				GlobalVariables.will_change = True
			elif op == '3':
				while True:
					print(f'{GlobalVariables.controller.name}拥有的道具:{GlobalVariables.controller.got_items}')
					print("""
					1：使用小刀（该发子弹会获得双倍伤害）
					2：饮用啤酒（退出当前子弹）
					3：使用放大镜（查看当前子弹）
					4：使用手铐（令对方跳过1回合）
					5：香烟（回复1点生命值）
					6：手机（随机获取一颗子弹的信息）
					7：肾上腺素（偷取对方的物品并立即使用）
					8：转换器（转换该颗子弹类型）
					9：小药丸（60%减少自己一滴血，40%增加两滴血）
					0：结束道具使用
					""")
					option = input('请选择要使用的道具')
					if option in [str(i) for i in range(0, 10)]:
						use_item(option)
						break

					print('输入错误，请重新输入')

			else:
				print('输入错误，请重新输入')

			if Player1.hp <= 2 and GlobalVariables.rounds == 3:
				Player1.down = True
				print(f'{Player1.name}的血量小于等于2，将无法加血，并且一枪便会死亡')

			if Player2.hp <= 2 and GlobalVariables.rounds == 3:
				Player2.down = True
				print(f'{Player2.name}的血量小于等于2，将无法加血，并且一枪便会死亡')

		else:
			if GlobalVariables.controller.hp <= 0 or GlobalVariables.enemy.hp <= 0:
				return True
			elif GlobalVariables.index >= len(Gun.bullets):
				print('子弹打空，已重新装填')

	def use_item(op):
		if op == '1':
			if '小刀' in GlobalVariables.controller.got_items:
				print('你将枪管锯短，获得双倍伤害（仅该发子弹有效）')
				Gun.damage = 2
				GlobalVariables.controller.got_items.remove('小刀')
				GlobalVariables.controller.knife_used += 1
			else:
				print('你没有该道具，请重新输入')

		elif op == '2':
			if '啤酒' in GlobalVariables.controller.got_items:
				if Gun.bullets[GlobalVariables.index]:
					print('退出了一发实弹')
				else:
					print('退出了一发空弹')
				GlobalVariables.index += 1
				GlobalVariables.controller.got_items.remove('啤酒')
				GlobalVariables.controller.beer_used += 1
			else:
				print('你没有该道具，请重新输入')

		elif op == '3':
			if '放大镜' in GlobalVariables.controller.got_items:
				if Gun.bullets[GlobalVariables.index]:
					print('这是一发实弹')
				else:
					print('这是一发空弹')
				GlobalVariables.controller.got_items.remove('放大镜')
				GlobalVariables.controller.glass_used += 1
			else:
				print('你没有该道具，请重新输入')

		elif op == '4':
			if '手铐' in GlobalVariables.controller.got_items:
				print('你使用手铐，对方的下一回合将会跳过')
				GlobalVariables.will_change = False
				GlobalVariables.controller.got_items.remove('手铐')
				GlobalVariables.controller.handcuff_used += 1
			else:
				print('你没有该道具，请重新输入')

		elif op == '5':
			if '香烟' in GlobalVariables.controller.got_items:
				if GlobalVariables.rounds != 3:
					print('吸入一根香烟，增加了1点生命值')
					GlobalVariables.controller.hp += 1
					GlobalVariables.controller.smoke_used += 1
					if GlobalVariables.controller.hp > GlobalVariables.higest_hp[GlobalVariables.rounds]:
						GlobalVariables.controller.hp = GlobalVariables.higest_hp[GlobalVariables.rounds]

				if GlobalVariables.rounds == 3 and GlobalVariables.controller.hp <= 2:
					print('您的血量少于2，无法加血，但仍然使用了香烟')
					GlobalVariables.controller.smoke_used += 1

				GlobalVariables.controller.got_items.remove('香烟')
			else:
				print('你没有该道具，请重新输入')

		elif op == '6':
			if '手机' in GlobalVariables.controller.got_items:
				input('信息仅允许持枪者了解，请对方回避。\n按回车继续')
				i = random.randint(0, Gun.bullets_num - 1)
				while GlobalVariables.index >= i:
					i = random.randint(0, Gun.bullets_num - 1)

				if Gun.bullets[i]:
					input(f'第{i + 1}发是实弹，回车进行下一步')
					print('\n' * 50)
				else:
					input(f'第{i + 1}发是空弹，回车进行下一步')
					print('\n' * 50)
				GlobalVariables.controller.got_items.remove('手机')
				GlobalVariables.controller.phone_used += 1
			else:
				print('你没有该道具，请重新输入')

		elif op == '7':
			item_dict = {
				'1': '小刀',
				'2': '啤酒',
				'3': '放大镜',
				'4': '手铐',
				'5': '香烟',
				'6': '手机',
				'7': '肾上腺素',
				'8': '转换器',
				'9': '小药丸'
			}
			if '肾上腺素' in GlobalVariables.controller.got_items:
				print(GlobalVariables.enemy.got_items)
				use = input('请选择对方的道具，选择后将会立即使用（使用道具编号，如 肾上腺素 -> 7）\n或输入q退出')
				if use == 'q':
					pass

				elif item_dict[use] in GlobalVariables.enemy.got_items:
					GlobalVariables.enemy.got_items.remove(item_dict[use])
					GlobalVariables.controller.got_items.append(item_dict[use])
					use_item(use)

				elif use == '7':
					print('不允许偷取肾上腺素，请重新选择')

				else:
					print('对方没有该道具，无法偷取')

				GlobalVariables.controller.epinephrine_used += 1
				GlobalVariables.controller.got_items.remove('肾上腺素')
			else:
				print('你没有该道具')

		elif op == '8':
			if '转换器' in GlobalVariables.controller.got_items:
				Gun.bullets[GlobalVariables.index] = not Gun.bullets[GlobalVariables.index]
				print('转换成功')

				GlobalVariables.controller.changer_used += 1
				GlobalVariables.controller.got_items.remove('转换器')
			else:
				print('你没有该道具')

		elif op == '9':
			if '小药丸' in GlobalVariables.controller.got_items:
				a = random.randint(1, 100)
				if a <= 60:
					GlobalVariables.controller.hp -= 1
					print(f'哦~运气真不好，扣除一滴血,剩余{GlobalVariables.controller.hp}滴')
				if a > 60:
					if GlobalVariables.rounds == 3 and GlobalVariables.controller.hp <= 2:
						print('您的血量少于2，无法加血，但仍然使用了药丸')
					else:
						GlobalVariables.controller.hp += 2
						print(f'哇塞！运气真好，增加两滴血,剩余{GlobalVariables.controller.hp}滴')
						if GlobalVariables.controller.hp > GlobalVariables.higest_hp[GlobalVariables.rounds]:
							GlobalVariables.controller.hp = GlobalVariables.higest_hp[GlobalVariables.rounds]

				GlobalVariables.controller.medicine_used += 1
				GlobalVariables.controller.got_items.remove('小药丸')
			else:
				print('你没有该道具')

		elif op == '0':
			print('道具使用结束')
			return None

		else:
			print('输入错误，请重新输入')

	GlobalVariables.controller = Player1
	GlobalVariables.enemy = Player2

	if GlobalVariables.rounds == 1:
		least = 3
		most = 4
	elif GlobalVariables.rounds == 2:
		Player1.hp, Player2.hp = 4, 4
		least = 6
		most = 8
	elif GlobalVariables.rounds == 3:
		Player1.hp, Player2.hp = 6, 6
		least = 6
		most = 8

	while True:
		if GlobalVariables.rounds >= 2:
			give_items()
		if shot():
			break


def give_items():
	print('正在发放道具')
	item_list = ['小刀', '啤酒', '放大镜', '手铐', '香烟', '手机', '肾上腺素', '转换器', '小药丸']
	i1, i2 = 0, 0
	if GlobalVariables.rounds == 2:
		print('本回合发放2个道具')
		while len(Player1.got_items) < 8 and i1 < 2:
			Player1.got_items.append(random.choice(item_list))
			i1 += 1
		while len(Player2.got_items) < 8 and i2 < 2:
			Player2.got_items.append(random.choice(item_list))
			i2 += 1
	elif GlobalVariables.rounds == 3:
		print('本回合发放4个道具')
		while len(Player1.got_items) < 8 and i1 < 4:
			Player1.got_items.append(random.choice(item_list))
			i1 += 1
		while len(Player2.got_items) < 8 and i2 < 4:
			Player2.got_items.append(random.choice(item_list))
			i2 += 1
	print('\n以下是玩家的道具列表：')
	print(f'{Player1.name}拥有的道具:{Player1.got_items}')
	print(f'{Player2.name}拥有的道具:{Player2.got_items}')


def update():  # 更新玩家信息并写入文件
	data_dict = readfile("data.json")
	data_list = data_dict["players"]
	index = 0
	while index < len(data_list):
		if data_list[index]["name"] == Player1.name:
			the_dict = data_list[index]
			if Player1.points > Player2.points:
				the_dict["win"] += 1
			elif Player2.points > Player1.points:
				the_dict["lost"] += 1
			the_dict["plays"] += 1
			the_dict["shots"] += Player1.shots
			the_dict["hurts"] += Player1.hurts
			the_dict["have_hurts"] += Player1.have_hurts
			the_dict["knife_used"] += Player1.knife_used
			the_dict["beer_used"] += Player1.beer_used
			the_dict["glass_used"] += Player1.glass_used
			the_dict["handcuff_used"] += Player1.handcuff_used
			the_dict["smoke_used"] += Player1.smoke_used
			the_dict["phone_used"] += Player1.phone_used
			the_dict["epinephrine_used"] += Player1.epinephrine_used
			the_dict["changer_used"] += Player1.changer_used
			the_dict["medicine_used"] += Player1.medicine_used
		elif data_list[index]["name"] == Player2.name:
			the_dict = data_list[index]
			if Player1.points < Player2.points:
				the_dict["win"] += 1
			elif Player2.points < Player1.points:
				the_dict["lost"] += 1
			the_dict["plays"] += 1
			the_dict["shots"] += Player2.shots
			the_dict["hurts"] += Player2.hurts
			the_dict["have_hurts"] += Player2.have_hurts
			the_dict["knife_used"] += Player2.knife_used
			the_dict["beer_used"] += Player2.beer_used
			the_dict["glass_used"] += Player2.glass_used
			the_dict["handcuff_used"] += Player2.handcuff_used
			the_dict["smoke_used"] += Player2.smoke_used
			the_dict["phone_used"] += Player2.phone_used
			the_dict["epinephrine_used"] += Player2.epinephrine_used
			the_dict["changer_used"] += Player2.changer_used
			the_dict["medicine_used"] += Player2.medicine_used
		index += 1
	writefile("data.json", data_dict)


def show_stats(name):  # 展示统计信息: 总游戏数，总胜利游戏数，总失败游戏数，总胜率|总承伤，总造成伤害，总道具使用情况
	data_list = readfile("data.json")["players"]
	index = 0
	while index < len(data_list):
		if data_list[index]['name'] == name:
			data_dict = data_list[index]
			print(f'{name}的统计信息如下：')
			print(f"""
游玩次数（登录次数）: {data_dict['plays']}
胜利场数: {data_dict['win']}
失败场数: {data_dict['lost']}
胜率: {data_dict['win'] / data_dict['plays'] if data_dict['plays'] != 0 else 0}
发射子弹数：{data_dict['shots']}
共造成伤害（不包括对自己造成的伤害）: {data_dict['hurts']}
共受到伤害（包括对自己造成的伤害）: {data_dict['have_hurts']}
小刀使用次数: {data_dict['knife_used']}
啤酒使用次数: {data_dict['beer_used']}
放大镜使用次数: {data_dict['glass_used']}
手铐使用次数: {data_dict['handcuff_used']}
香烟使用次数: {data_dict['smoke_used']}
手机使用次数：{data_dict['phone_used']}
肾上腺素使用次数：{data_dict['epinephrine_used']}
转换器使用次数：{data_dict['changer_used']}
小药丸使用次数：{data_dict['medicine_used']}
""")
		index += 1


def main():
	if not start():
		quit()

	introduce()
	for i in range(15):
		print('\n')

	while True:
		restart()
		flag = True
		while GlobalVariables.rounds <= 3:
			if flag:
				op = input('输入1开始游戏；输入2展示统计信息')
			if op == '1':
				flag = False
				fight()

				if Player1.hp <= 0:
					Player2.points += 1
					GlobalVariables.rounds += 1
					print(f'{Player1.name} 死亡。{Player2.name} 胜利，共胜利了{Player2.points}局')
					if GlobalVariables.rounds < 3:
						print(f'接下来进入第{GlobalVariables.rounds}局\n')

				elif Player2.hp <= 0:
					Player1.points += 1
					GlobalVariables.rounds += 1
					print(f'{Player2.name} 死亡。{Player1.name} 胜利，共胜利了{Player1.points}局')
					if GlobalVariables.rounds < 3:
						print(f'接下来进入第{GlobalVariables.rounds}局\n')
			elif op == '2':
				op2 = input(f"""
	查看谁的统计信息？
	1：{Player1.name}
	2：{Player2.name}
	3: 两人的统计信息
	""")
				if op2 == '1' or op2 == Player1.name:
					show_stats(Player1.name)
				elif op2 == '2' or op2 == Player2.name:
					show_stats(Player2.name)
				elif op2 == '3':
					show_stats(Player1.name)
					show_stats(Player2.name)
				else:
					print('输入错误')
			else:
				print('输入错误，请重新输入')

		print(f'结算:\n{Player1.name} 共胜利 {Player1.points} 局，{Player2.name} 共胜利 {Player2.points} 局')
		if Player1.points > Player2.points:
			print(f'{Player2.name} 最终还是败下阵来，{Player1.name} 获得了最终的胜利')
		elif Player1.points < Player2.points:
			print(f'{Player1.name} 最终还是败下阵来，{Player2.name} 获得了最终的胜利')

		update()
		op3 = input('输入q退出游戏,输入其他则重新开始')
		if op3.strip().lower() == 'q':
			quit()


if __name__ == '__main__':
	main()
