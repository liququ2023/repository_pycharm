# 十进制小数转换为二进制

def decimal2bin(dec):
    # 乘2取整
    result = ['0.']
    for i in range(100):
        dec = dec * 2
        dec_int = int(dec)
        result.append(str(dec_int))
        dec = dec - dec_int
        if dec == 0:
            break
    return ''.join(result)


num = float(input("请输入一个十进制小数："))
num_bin = decimal2bin(num)
print(f'转换为二进制形式：{num_bin}')
