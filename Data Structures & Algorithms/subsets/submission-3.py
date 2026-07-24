class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        subsets = {"-":[]}
        for i in nums:
            subsets[str(sorted(set([i])))] = list(set([i]))
        for i in nums:
            temps = subsets.copy()
            for sublist in temps.values():
                hashed = set(sublist + [i])
                subsets[str(sorted(hashed))] = list(hashed)
            # print(subsets)
        return list(subsets.values())

                



        