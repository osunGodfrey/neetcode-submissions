class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        op = set("+-*/")
        for e in tokens:
            if e in op:
                right = int(stack.pop())
                left = int(stack.pop())
                if e == "+":
                    stack.append(left + right)
                elif e == "-":
                    stack.append(left - right)
                elif e == "*":
                    stack.append(left * right)
                elif e == "/":
                    stack.append(left / right)
                else:
                    return None
            else:
                stack.append(e)
        return int(stack.pop())

        