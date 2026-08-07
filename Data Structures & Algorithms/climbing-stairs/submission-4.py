class Solution:
    def climbStairs(self, n: int) -> int:
        minus1 = 0
        minus2 = 0
        for i in range(n):
            print(minus1, minus2)
            if i == 0:
                minus1 = 1
            # if i == 1:
            #     minus2 = 1
            temp = minus1 + minus2
            minus2 = minus1
            minus1 = temp
            # print(temp)
        return minus1
        