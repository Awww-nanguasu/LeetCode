#

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits)
        carry = 1

        for i in range(-1, -length-1, -1):
            tmp = digits[i] + carry
            if tmp >= 10:
                digits[i] = tmp % 10
                carry = tmp // 10
            else:
                carry = 0
                digits[i] = tmp
            
        if carry:
            digits.insert(0, carry)

        return digits