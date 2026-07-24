import bisect
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.nums = nums
        self.nums.sort()
        self.k = k
        

    def add(self, val: int) -> int:
        # print(self.nums)
        index = bisect.bisect_left(self.nums, val)
        self.nums.insert(index, val)
        return self.nums[-1 * self.k]
        
