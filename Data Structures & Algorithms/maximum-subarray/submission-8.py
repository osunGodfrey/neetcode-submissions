class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        maxvalue = -999
        maxsub = [0] * len(nums)
        totalsum = [0] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            if i == len(nums) - 1:
                maxsub[i] = nums[i]
                maxvalue = max(maxvalue, maxsub[i])
                continue
            maxsub[i] = maxsub[i + 1] + nums[i]
            if maxsub[i] <= nums[i]:
                maxsub[i] = nums[i]
            maxvalue = max(maxvalue, maxsub[i])
            # print(maxsub)
        return maxvalue
            
            
        