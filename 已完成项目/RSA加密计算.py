# coding:utf-8
import math
import random


def primary_number(num):
	for i in range(2, int(math.sqrt(num)) + 1):
		if num % i == 0:
			return False
	return True


def get_keys(first_primary_number, second_primary_number):
	first_public_key = first_primary_number * second_primary_number  # 获得第一个公钥
	temp_number = (first_primary_number - 1) * (second_primary_number - 1)  # 取临时数

	possible_second_public_keys = []  # 获取可能的第二个公钥
	for i in range(temp_number, temp_number + 10001):  # 遍历比临时数大10000之内的数
		if math.gcd(i, temp_number) == 1:  # 如果最大公约数为一
			possible_second_public_keys.append(i)  # 将其加入可能
	second_public_key = random.choice(possible_second_public_keys)  # 确定第二个公钥

	private_key = None
	for private_key in range(1, temp_number):  # 获取私钥
		if private_key * second_public_key % temp_number == 1:
			break

	return first_public_key, second_public_key, private_key


def encode(plaintext, first_public_key, second_public_key):
	plaintext_codes = [ord(i) for i in plaintext]  # 获取明文每个字符的unicode编码
	ciphertext = ''
	for plaintext_code in plaintext_codes:  # 遍历明文编码
		if plaintext_code > first_public_key:
			print("第一个公钥过小，请重新开始计算")
			return -1
		ciphertext += chr(plaintext_code ** second_public_key % first_public_key)  # 计算密文
	print(f'密文是\n{ciphertext}')


def decode(ciphertext, private_key, first_public_key):
	ciphertext_codes = [ord(i) for i in ciphertext]
	plaintext = ''
	for ciphertext_code in ciphertext_codes:
		plaintext += chr(ciphertext_code ** private_key % first_public_key)
	print(f"明文是\n{plaintext}")


def main():
	while True:
		mode = input("请输入模式\n1:加密, 2:解密, q:退出\n")
		if mode == "1":
			while True:
				first_primary_number = input("请输入第一个质数")
				second_primary_number = input("请输入第二个质数")

				if not first_primary_number.isdecimal():  # 检查非法输入情况
					print("非法输入，请输入整数")
				elif not second_primary_number.isdecimal():
					print("非法输入，请输入整数")
				first_primary_number, second_primary_number = int(first_primary_number), int(second_primary_number)	 # 将字符串转为整数

				if not primary_number(first_primary_number):  # 检查质数情况
					print(f"{first_primary_number}不是质数，请重新输入")
					continue
				elif not primary_number(second_primary_number):
					print(f"{second_primary_number}不是质数，请重新输入")
					continue
				break

			first_public_key, second_public_key, private_key = get_keys(first_primary_number, second_primary_number)
			plaintext = input("请输入明文")
			will_restart = encode(plaintext, first_public_key, second_public_key)
			if will_restart == -1:
				continue

			print("请记好以下数据：")
			print(f"第一个公钥：{first_public_key}")
			print(f"第二个公钥：{second_public_key}")
			print(f"私钥：{private_key}")

		elif mode == "2":
			first_public_key = int(input('请输入第一个公钥'))
			private_key = int(input('请输入私钥'))
			ciphertext = input('请输入密文')
			decode(ciphertext, private_key, first_public_key)

		elif mode.capitalize() == 'Q':
			quit()

		else:
			print("输入错误，请重新输入")
			continue


if __name__ == '__main__':
	main()
