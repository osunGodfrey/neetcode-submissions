class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        left_prod = [1] * len(nums)
        acc_prod = 1
        for i in range(len(nums) - 1, 0, -1):
            acc_prod = acc_prod * nums[i]
            left_prod[i - 1] = acc_prod
        # return left_prod

        right_prod = [1] * len(nums)
        acc_prod = 1
        for i in range(len(nums) - 1):
            acc_prod = acc_prod * nums[i]
            right_prod[i + 1] = acc_prod
            # print(nums[i+1])
        # return (right_prod + left_prod)
        acc_prod = [0] * len(nums)
        for i in range(len(nums)):
            acc_prod[i] = left_prod[i] * right_prod[i]
        return acc_prod

