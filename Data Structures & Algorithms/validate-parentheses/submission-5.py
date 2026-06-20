class Solution:
    def isValid(self, s: str) -> bool:
        left_brack = set("({[")
        right_brack = set(")}]")
        reflect_brack = {"(":")", "{":"}", "[":"]", "$":"$"}
        stack = ["$"]
        stack_size = 1
        for br in s:
            # print(br)
            # print(stack)
            if br in left_brack:
                stack.append(br)
                stack_size += 1
            elif br in right_brack:
                # print(stack[stack_size - 1], br ,br == stack[stack_size - 1])
                if br == reflect_brack[stack[stack_size - 1]]:
                    stack.pop()
                    stack_size -= 1
                else:
                    return False
        if len(stack) > 1:
            return False
        else:
            return True
                