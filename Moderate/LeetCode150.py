class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        for x in tokens:
            if x.isdigit():
                stack.append(int(x))
            elif (x.split('-')[-1]).isdigit():
                stack.append(-int(x.split('-')[-1]))
            else:
                a = stack.pop()
                b = stack.pop()
                if x == '+':
                    stack.append(a+b)
                elif x == '-':
                    stack.append(b-a)
                elif x == '*':
                    stack.append(a*b)
                else:
                    res = abs(b)//abs(a)
                    if a*b<0:
                        res = -res
                    stack.append(res)
        return stack[0]