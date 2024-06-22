print('Hello\nworld')  # 换行(New line)
print('Hello\tworld')  # 制表符(一个tab）（Hell o*** worl d***)
print('Hello***\tworld')
print('Hello\rworld')  # 回车，将光标移至开头，world覆盖了Hello(Return)
print('Hello\bworld')  # 退格，无需解释（backspace）
print('老师说:\"小明考了100分\"')  # 让单/双引号变成字符串，而不是表示字符串的边缘
print('H:\\.minecraft\\mods\\')  # 让反斜杠成为字符串，而不是表达转义字符
# 原字符，让字符串里的转义字符失效，在字符串前加‘r’。
print(r'\n表示换行')
