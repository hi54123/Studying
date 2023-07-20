# coding=UTF-8
while True:
    mode = input('模式(1 中转Unicode，2 Unicode转中）：')
    if mode == '1':
        a = input('输入文字:\n')
        a = a.strip()
        for i in a:
            b = ord(i)
            c = hex(b)
            print(c, end=' ')
        break
    
    elif mode == '2':
        a = input('输入Unicode数值,以空格分隔:\n')
        a = a.strip()
        a = a.split(" ")
        for i in a:
            i = chr(int(i, 16))
            print(i, end='')
        break
    
    else:
        print('非法输入')
        continue
    