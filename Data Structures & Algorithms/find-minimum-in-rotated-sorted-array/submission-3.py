class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[len(nums) - 1]
        last_min_val = nums[0]
        min_index = len(nums) - 1
        last_min_index = 0
        while(True):
            # print(nums[last_min_index: min_index])
            if last_min_val < min_val:
                delta = len(nums[last_min_index: min_index])  // 2
                if delta <= 0: break
                if nums[min_index - delta] < min_val:
                    min_val = nums[min_index - delta]
                    min_index = min_index - delta
                else:
                    last_min_val = nums[min_index - delta]
                    last_min_index = min_index - delta
            else:
                delta = len(nums[last_min_index: min_index])  // 2
                if delta <= 0: break
                if nums[min_index - delta] < min_val:
                    min_val = nums[min_index - delta]
                    min_index = min_index - delta
                else:
                    last_min_val = nums[min_index - delta]
                    last_min_index = min_index - delta
        if nums[min_index] < nums[last_min_index]:
            return nums[min_index]
        else:
            return nums[last_min_index]


