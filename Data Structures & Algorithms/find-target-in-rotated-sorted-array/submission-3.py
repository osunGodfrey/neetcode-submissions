class Solution:
    def findMin(self, nums: List[int]) -> int:
        min_val = nums[len(nums) - 1]
        last_min_val = nums[0]
        min_index = len(nums) - 1
        last_min_index = 0
        while(True):
                delta = len(nums[last_min_index: min_index])  // 2
                if delta <= 0: break
                if nums[min_index - delta] < min_val:
                    min_val = nums[min_index - delta]
                    min_index = min_index - delta
                else:
                    last_min_val = nums[min_index - delta]
                    last_min_index = min_index - delta
        if nums[min_index] < nums[last_min_index]:
            return min_index
        else:
            return last_min_index

    def search(self, nums: List[int], target: int) -> int:
        off = self.findMin(nums)
        print(off)
        print(nums[:off])
        print(nums[off:])
        nums = nums[off:] + nums[:off]
        print("sorted", nums)
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
                return (i + off) % len(nums)
            elif step <= 0:
                return -1
            else:
                return None
            # step = (max_i - min_i) // 2
            # count += 1
            if step <= 0: return -1
            # if count == 5: return -4
            # print("------")
        return -1
        
        
        