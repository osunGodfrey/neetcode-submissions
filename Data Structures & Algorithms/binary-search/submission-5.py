import math
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if nums[0] > target:
            return -1
        size = len(nums)
        step = size
        max_i = size
        min_i = 0
        i = 0
        count = 0
        while i < size:
            step = math.ceil((max_i - min_i) / 2)
            # print("step", step)
            # print("min", min_i, "max", max_i)
            # print("index", i,"value", nums[i], "targe", target)
            if nums[i] < target:
                min_i = i + step
                i = i + step
                # print("-->", i)
            elif nums[i] > target:
                max_i = i
                min_i = i - step
                i = i - step
                # print("<--", i)
            elif nums[i] == target:
                # print("==", i)
                return i
            elif step <= 4:
                return -2
            else:
                return None
            # step = (max_i - min_i) // 2
            # count += 1
            if step <= 0: return -1
            # if count == 5: return -4
            # print("------")
        return -1
        