class Solution:
    def run(self, nums):
        # nums.pop()
        cash = [0] * len(nums)
        if len(nums) >= 1:
            cash[0] = nums[0]
        if len(nums) >= 2:
            cash[1] = nums[1]
        if len(nums) >= 3:
            cash[2] = nums[2] + nums[0]
        if len(nums) < 4:
            return max(cash[len(nums) - 1], cash[len(nums) - 2])
        for i in range(3, len(nums), 1):
            step2 = nums[i] + cash[i - 2]
            step3 = nums[i] + cash[i - 3]
            cash[i] = max(step2, step3)
            # print(i)
            # cash[i] = cash[i] + nums
        print(cash)
        return max(cash[len(nums) - 1], cash[len(nums) - 2])
        
    def rob(self, nums: List[int]) -> int:
        # nums.pop()
        if len(nums) == 1:
            return nums[0]
        return max(self.run(nums[1:]), self.run(nums[:len(nums) - 1]))