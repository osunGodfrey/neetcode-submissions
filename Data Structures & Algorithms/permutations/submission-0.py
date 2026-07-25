class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        combinations = []
        def recurse(state, nums):
            # print("state:", state, "nums:", nums)
            if nums is None:
                return None
            if len(nums) < 1:
                combinations.append(state)
                return None
            n = len(nums)
            # print("i:", n, ":", nums)
            for i in range(n):
                new_state = state + [nums[i]]
                poped = nums.pop(i)
                # print("new state:", new_state, "nums:", nums)
                recurse(new_state, nums)
                nums.insert(i, poped)
            return
        recurse([], nums)
        # print(combinations)
        return combinations

        