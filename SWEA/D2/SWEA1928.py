base64 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '+', '/']
base64_encode = dict(enumerate(base64))

def my_bi(x):
    num = x
    bi = ''
    while num // 2 != 0:
        bi += str(num % 2)
        num = num // 2
    if num == 1:
        bi += '1'
    bi = bi[::-1]
    return '{0:0>6}'.format(bi)

def my_de(x):
    num = x[::-1]
    result = 0
    for key, bi in dict(enumerate(num)).items():
        if int(bi) == 1:
            result += 2 ** key
    return result

tc = int(input())

for i in range(1, tc + 1):
    litter = input()
    decode = []
    for text in litter:
        for key, lit in base64_encode.items():
            if text == lit:
                decode.append(key)

    decode_bi = ''
    for num in decode:
        decode_bi += my_bi(num)

    new_decode = []

    for k in range(0, len(decode_bi), 8):
        new_decode.append(decode_bi[k : k + 8])

    new_string = ''

    for string in new_decode:
        new_string += chr(my_de(string))
    print('#{} {}'.format(i, new_string))