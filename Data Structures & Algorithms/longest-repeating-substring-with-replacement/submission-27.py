from collections import Counter
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        maxfreq = 0
        freqdict = {}
        def replace(substring, k):
            nonlocal maxfreq
            fchar = substring[-1]
            if fchar in freqdict:
                freqdict[fchar] += 1
                maxfreq = max(maxfreq, freqdict[fchar])
            else:
                freqdict[fchar] = 1
                maxfreq = max(maxfreq, freqdict[fchar])
            # print(freqdict)
            # print(maxfreq)
            # max_freq = max(letters.values())
            all_freq = len(substring)
            if (all_freq - maxfreq) <= k:
                return True
            else:
                ichar = substring[0]
                if ichar in freqdict:
                    freqdict[ichar] -= 1
                    if freqdict[ichar] == 0:
                        del freqdict[ichar]
                return False
        i = 0
        j = 0
        while(j < len(s)):
            # print(s[i:j])
            if replace(s[i:min(j + 1, len(s))], k):
                j += 1
            else:
                i += 1
                j += 1
        # print(s[i:j])
        return len(s[i:j])


        