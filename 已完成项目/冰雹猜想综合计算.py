# coding:utf-8


while True:
	print('1:区域内&次数 2：区域&文件 3：过程&单数&次')
	op = input('请选择模式：')
	
	# 1区:区域&次数
	if op == '1':
		o = int(input('输入起始数：'))
		e = int(input('输入结束数:'))
		t = 0
		for a in range(o, e + 1):
			b = a
			while a != 1:
				t += 1
				if a % 2 == 0:
					a //= 2
				else:
					a = a * 3 + 1
			print(f'结果为{a}')
			print(f'{b}用了（{t}）次变成1')
			print('\n', end='')
		op2 = input('是否退出（y/n)')
		if op2 == 'y':
			break
	
	# 2区：区域&文件
	elif op == '2':
		r1 = int(input('请输入开始的数'))
		r2 = int(input('请输入结束的数+1'))
		out = open(input('您想将结果输出至哪里，请输入路径(没有则创建一个):'), "w")
		for a in range(r1, r2):
			t = 0
			b = a
			while a != 1:
				t = t + 1
				if a % 2 == 0:
					a //= 2
				else:
					a = a * 3 + 1
			out.write(f'{b}用了（{t}）次变成1')
		out.close()
		op2 = input('是否退出（y/n)')
		if op2 == 'y':
			break
	
	# 3区：过程，次数，仅一个数
	elif op == '3':
		a = int(input('输入一个自然数：'))
		b = a
		t = 0
		while a != 1:
			t += 1
			
			if a % 2 == 0:
				a //= 2
			else:
				a = a * 3 + 1
			
			print(a)
		print(f'{b}用了（{t}）次变成1')
		op2 = input('是否退出（y/n)')
		if op2 == 'y':
			break
	
	else:
		print('输入错误，请输入1或2或3')
		continue
