class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [item for sublist in matrix for item in sublist]
        if nums[0] > target:
            return False
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
                return True
            elif step <= 0:
                return False
            else:
                return None
            # step = (max_i - min_i) // 2
            # count += 1
            if step <= 0: return False
            # if count == 5: return -4
            # print("------")
        return False