class Solution:
    def calculate(self, s: str) -> int:
        res = curr = 0
        sign = 1
        stack =[]

        for x in s:
            if x.isdigit():
                curr = curr*10+int(x)
            elif x in ["+","-"]:
                res += curr*sign
                sign = 1 if x=="+" else -1
                curr = 0

            elif x=="(":
                stack.append(res)
                stack.append(sign)
                res=0
                sign=1

            elif x==")":

                res += sign*curr 
                res *= stack.pop()
                res += stack.pop()
                curr = 0

        return res + curr*sign

        