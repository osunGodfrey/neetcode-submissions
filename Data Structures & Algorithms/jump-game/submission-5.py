class Solution:
    def canJump(self, nums: List[int]) -> bool:
        valid = [False] * len(nums)
        last_valid = len(nums)
        for i in range(len(nums), 0, -1):
            if i == len(nums):
                valid[i - 1] = True
                last_valid = i - 1
                # print(valid)
                continue
            if (i - 1 + nums[i - 1]) >= last_valid:
                valid[i - 1] = True
                last_valid = i - 1
                # print(valid)
        return valid[0]

            
        