class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sdict = {}
        tdict = {}
        kset = set()
        for val in s:
            sdict[val] = sdict.get(val, 0) + 1
            kset.add(val)
        for val in t:
            tdict[val] = tdict.get(val, 0) + 1
            kset.add(val)
        for k in kset:
            if sdict.get(k, -1) != tdict.get(k, -2):
                return False
        return True

        