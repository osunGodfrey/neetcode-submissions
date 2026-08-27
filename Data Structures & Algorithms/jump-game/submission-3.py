class Solution:
    def canJump(self, nums: List[int]) -> bool:
        valid = [False] * len(nums)
        for i in range(len(nums), 0, -1):
            # print(i - 1)
            if i == len(nums):
                valid[i - 1] = True
                # print(valid)
                continue
            for j in range(nums[i - 1]):
                # print((i - 1), (i - 1 + (j + 1)))
                if (i - 1 + (j + 1)) > len(nums) - 1:
                    break
                if valid[i - 1 + (j + 1)]:
                    valid[i - 1] = True
                # print(valid)
        return valid[0]
            


        