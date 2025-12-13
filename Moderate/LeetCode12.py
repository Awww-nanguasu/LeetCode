
#hashmap and recursion ⭐
class Solution:
    dict = {1:'I', 4:'IV', 5:'V', 9:'IX', 
            10:'X', 40:'XL', 50:'L', 90:'XC',
            100:'C', 400:'CD', 500:'D', 900:'CM'}

    def intToRoman(self, num: int) -> str:
        if num == 0:
            return ''
    
        if num>= 1000:
            return 'M' + self.intToRoman(num - 1000)

        else:
            n = int(log10(num))
            loc_array = [1*10**(n), 4*10**(n), 5*10**(n), 9*10**(n)]

            if num>=loc_array[3]:
                str = self.dict[loc_array[3]]
                return str + self.intToRoman(num - loc_array[3])

            for i in range(3):
                if (num>=loc_array[i]) and (num<loc_array[i+1]):
                    str = self.dict[loc_array[i]]
                    return str + self.intToRoman(num - loc_array[i])
        