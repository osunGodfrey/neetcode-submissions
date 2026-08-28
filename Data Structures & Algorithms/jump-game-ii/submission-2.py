class Solution:
    def jump(self, nums: List[int]) -> int:
        minstep = [999] * len(nums)
        for i in range(len(nums) - 1, -1, -1):
            # print(i)
            if i == len(nums) - 1:
                minstep[i] = 0
                # print(minstep)
                continue
            skips = nums[i]
            if i + skips >= len(nums):
                skips = len(nums) - 1
            # print(minstep[i + 1:i + 1 + skips])

            minstep[i] = min(minstep[i + 1:i + 1 + skips]) + 1 if len(
                minstep[i + 1:i + 1 + skips]) > 0 else 999
            # print(minstep)
        return minstep[0]


        