import math
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        nums = [item for sublist in matrix for item in sublist]
        if nums[0] > target:
            return False
        i = 0
        l = 0
        m = 0
        n = len(matrix[0])
        col = len(matrix)
        size = n * col
        step = size
        max_i = size
        min_i = 0
        # count = 0
        while i < size:
            step = math.ceil((max_i - min_i) / 2)
            # print("step", step)
            # print("min", min_i, "max", max_i)
            # print("index", i,"value", nums[i], "targe", target)
            if matrix[l][m] < target:
                min_i = i + step
                i = i + step
                l = i // n
                m = i % n
                # print("-->", i)
            elif matrix[l][m] > target:
                max_i = i
                min_i = i - step
                i = i - step
                l = i // n
                m = i % n
                # print("<--", i)
            elif matrix[l][m] == target:
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