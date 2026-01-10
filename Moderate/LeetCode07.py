
# str2int 2 star
def reverse(x: int) -> int:    
    if abs(x) < 10:
        return x

    str_x = str(x)

    if str_x[0] == '-':
        str_x = '-' + str_x[:0:-1]
    else:
        str_x = str_x[::-1]
        
    x = int(str_x)
    if x < -2**31 or x > 2**31 - 1:
        return 0
    return x