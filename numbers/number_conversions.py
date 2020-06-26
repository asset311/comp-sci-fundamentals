def decimal_to_binary(n:int) -> str:
    
    if n == 0:
        res = '0'
    else:
        res = ''

    stack = []
    while n>0:
        stack.append(str(n%2))
        n = n // 2
    while stack:
        res += stack.pop()
    
    return res

def binary_to_decimal(b:str) -> int:
    num = exp = 0
    for i in reversed(range(len(b))):
        if b[i] == '1':
            num += 2**exp
        else:
            num += 0
        exp += 1
    return num

# two's complement
def int_to_hex(n:int) -> str:
    stack = []  #used to store remainders
    int_to_hex = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
    
    if n == 0:
        return '0'
    elif n<0:   #convert the base if negative
        n *=-1
        n = pow(2,32) - n
    
    while n>0:
        stack.append(n%16)
        n = n // 16
    
    res = ''
    while stack:
        i = stack.pop()
        res += str(i) if i<10 else int_to_hex[i]
    
    return res