from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = {};
        for word in strs:
            if frozenset(Counter(word).items()) in anaDict:
                anaDict[frozenset(Counter(word).items())].append(word)
            else:
                anaDict[frozenset(Counter(word).items())] = [word]
        # print(anaDict)
        # print(list(anaDict.values()))
        return list(anaDict.values())

        