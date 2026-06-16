class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        mid_index = len(nums) // 2
        if mid_index == 0: 
            return False

        if len(nums) == 2:
            if nums[0] == nums[1]: 
                return True
            else:
                return False

        if len(nums) == 3:
            if (nums[0] == nums[1]) or (nums[0] == nums[2]) or (nums[1] == nums[2]):
                return True
            else:
                return False

        if len(nums) == 4:
            if (nums[0] == nums[1]) or (nums[0] == nums[2]) or (nums[0] == nums[3]) or (nums[1] == nums[2] or nums[1] == nums[3]) or (nums[2] == nums[3]):
                return True
            else:
                return False

        mid_value = nums[mid_index]
        left_nums = []
        right_nums = []
        for i in range(len(nums)):
            if (nums[i] == mid_value) and not (i == mid_index):
                return True
            elif (nums[i] == mid_value) and (i == mid_index):
                continue
            elif nums[i] < mid_value:
                left_nums = left_nums + [nums[i]]
            else:
                right_nums = right_nums + [nums[i]]
        return self.hasDuplicate(left_nums) or self.hasDuplicate(right_nums)
        


        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if nums[i] == nums[j] and i != j:
        #             return True
        # return False

        # left, right = 0, 0
        # if len(nums) == 2:
        #     if nums[0] == nums[1]:
        #         return True 
        #     else: 
        #         return False
        # if len(nums) <= 1: return False
        # if len(nums) % 2 == 0:
        #     left_nums = nums[:len(nums) // 2 ]
        #     right_nums = nums[len(nums) // 2:]
        #     for l_index in range(len(left_nums)):
        #         for r_index in range(len(right_nums)):
        #             if left_nums[l_index] == right_nums[r_index]:
        #                 return True
        #     return self.hasDuplicate(left_nums) or self.hasDuplicate(right_nums)
        # else:
        #     left_nums = nums[:len(nums) // 2]
        #     right_nums = nums[len(nums) // 2 + 1:]
        #     for l_index in range(len(left_nums)):
        #         for r_index in range(len(right_nums)):
        #             if left_nums[l_index] == right_nums[r_index]:
        #                 return True
        #     return self.hasDuplicate(left_nums) or self.hasDuplicate(right_nums)


            
        