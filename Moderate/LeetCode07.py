
# str2int 2 star
# def reverse(x: int) -> int:    
#     if abs(x) < 10:
#         return x

#     str_x = str(x)

#     if str_x[0] == '-':
#         str_x = '-' + str_x[:0:-1]
#     else:
#         str_x = str_x[::-1]
        
#     x = int(str_x)
#     if x < -2**31 or x > 2**31 - 1:
#         return 0
#     return x

# Failed 
# In Python language: -123%10= -7 
# def reverse(x: int) -> int:    
#         res = 0
#         while x!=0:
#             tmp = x%10
#             if (res< -2**31 // 10) or (tmp<-8):
#                 return 0
            
#             if (res> (2**31 - 1) // 10) or (tmp>7):
#                 return 0
        
#             res = res*10 + tmp
#             print(res)
#             x //= 10
#         return res

def reverse(x: int) -> int:
    flag = 0
    if x < 0:
        flag = 1
        x = abs(x)

    res = 0
    while x!=0:
        tmp = x%10
    
        print(res>(2**31 - 1)//10)

        if (res> (2**31 - 1) // 10) or (res== (2**31 - 1) and tmp>7):
            return 0
        
        res = res*10 + tmp
        x //= 10

    if flag:
        res = -res
        if res< -2**31 -1:
            return 0

    return res

print(reverse(90000))