class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        combinations = {}
        def recurse(state):
            # print(state)
            # if len(state) > 5: return None
            if sum(state) == target:
                combinations[str((sorted(state)))] = state
                return None
            if sum(state) > target:
                return None
            hashed_states = []
            for i in nums:
                new_state = state + [i]
                if set(new_state) in hashed_states:
                    return None
                hashed_states.append(set(new_state))
                recurse(new_state)
            return None
        recurse([])
        # print(truthlist)
        # print(len(list(combinations.values())))
        return list(combinations.values())