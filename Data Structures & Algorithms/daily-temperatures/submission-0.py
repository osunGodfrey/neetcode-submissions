class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        i = 0
        stack = []
        results = [0] * len(temperatures)
        while(i < len(temperatures)):
            print(stack)
            while(len(stack) > 0):
                if stack[-1][0] < temperatures[i]:
                    val, j = stack.pop(-1)
                    results[j] = i - j
                else:
                    break
            stack.append([temperatures[i], i])
            i += 1
        # print(results)
        return results
