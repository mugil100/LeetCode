import operator as op
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op_map = {
            "+": op.add,
            "-": op.sub,
            "*": op.mul,
            "/": op.truediv
        }

        stack = []

        for x in tokens:
            if x=="+":
                stack.append(stack.pop()+stack.pop())
            elif x=="-":
                stack.append(-(stack.pop()-stack.pop()))
            elif x=="*":
                stack.append(stack.pop()*stack.pop())
            elif x=="/":
                a,b = stack.pop(),stack.pop()
                stack.append(int(b/a))
            else:
                stack.append(int(x))
        return stack[-1]