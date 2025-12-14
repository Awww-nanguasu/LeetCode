# Stack ⭐⭐

class Solution:
    dict = {')':'(', '}':'{', ']':'['}

    def isValid(self, s: str) -> bool:
        if len(s)%2!=0:
            return False

        heap = []
        for x in s:
            if x == '(' or x == '[' or x == '{':
                heap += x
            elif len(heap)==0 or heap[-1]!=self.dict[x]:
                return False
            else:
                heap.pop()
            
        if len(heap)!=0:
            return False
        
        return True