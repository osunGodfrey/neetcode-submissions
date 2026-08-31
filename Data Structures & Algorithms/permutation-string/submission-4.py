from collections import Counter
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        ss1 = set(Counter(s1).items())
        offset = len(s1)
        print("start")
        for i in range(offset, len(s2), 1):
            # print(ss1, set(Counter(s2[i - offset: i]).items()))
            if ss1 == set(Counter(s2[i - offset: i]).items()):
                return True
        if ss1 == set(Counter(s2[len(s2) - offset: len(s2) + 1]).items()):
                return True
        return False
        