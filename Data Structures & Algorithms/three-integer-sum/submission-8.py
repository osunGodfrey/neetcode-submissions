from collections import Counter
class Solution: 
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        offset = {}
        zeros = {}
        found = []
        for index, num in enumerate(nums):
            offset[num] = index
        for i, numi in enumerate(nums):
            for j, numj in enumerate(nums):
                leftoff = -(numi + numj)
                if leftoff in offset:
                    k = offset[leftoff]
                    if not (i == j or i == k or j == k):
                        if (numi + numj + leftoff ) == 0:
                            if zeros.get(frozenset((numi, numj, leftoff)), False):
                                # found.append([numi, numj, leftoff])
                                continue
                            else:
                                found.append([numi, numj, leftoff])
                                zeros[frozenset((numi, numj, leftoff))] = True   
        # print(zeros)
        # print(found)
        return found

        