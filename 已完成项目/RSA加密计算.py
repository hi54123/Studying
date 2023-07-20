# coding:utf-8
import math


# 定义质数验证函数
def primary_number(num):
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			print(f"{num}不是质数")
			return False
	return True


while True:
	options = input('请输入步骤（获取公钥(1) / 加密密码(2) / 解密(3）输入q退出：')
	if options == '获取公钥' or options == '1':
		while True:
			# 获取公钥
			first_primary_number = int(input('请输入第一个质数，退出请输入0\n'))
			if first_primary_number == 0:
				chooses = input('确定要退出吗(确定为y，否为任何)')
				if chooses == 'y':
					quit()
				else:
					continue
			second_primary_number = int(input('请输入第二个质数，退出请输入0\n'))
			if second_primary_number == 0:
				chooses = input('确定要退出吗(确定为y，否为任何)')
				if chooses == 'y':
					quit()
				else:
					continue
			if primary_number(first_primary_number):
				if primary_number(second_primary_number):
					first_public_key = first_primary_number * second_primary_number
					temp_number = (first_primary_number - 1) * (second_primary_number - 1)
					print('R=' + str(temp_number))
					second_public_key = int(input('请输入一个与R互质的数:\n'))
					print('公钥:' + str(first_public_key), str(second_public_key))
					# 获取私钥
					for private_key in range(1, temp_number):
						if private_key * second_public_key % temp_number == 1:
							break
					print(f'私钥是:{private_key}')
					break
				else:
					continue
			else:
				continue
	
	# 加密密码
	elif options == '加密密码' or options == '2':
		first_public_key = int(input('请输入第一个公钥'))
		second_public_key = int(input('请输入第二个公钥'))
		plaintext = input('请输入明文')
		plaintext_codes = [ord(i) for i in plaintext]
		ciphertext = ''
		for plaintext_code in plaintext_codes:
			ciphertext += chr(int(math.pow(plaintext_code, second_public_key)) % first_public_key)
		print(f'密文是\n{ciphertext}')
	
	# 解密
	elif options == '解密' or options == '3':
		# 接受到乙的C后：
		first_public_key = int(input('请输入第一个公钥'))
		private_key = int(input('请输入私钥'))
		ciphertext = input('请输入密文')
		ciphertext_codes = [ord(i) for i in ciphertext]
		plaintext = ''
		for ciphertext_code in ciphertext_codes:
			plaintext += chr(int(math.pow(ciphertext_code, private_key) % first_public_key))
		print(f'明文是：{plaintext}')
	
	elif options == 'q':
		quit()
		
	else:
		print('非法输入')
		continue
		