class Solution:
    encription = []

    def encode(self, strs: List[str]) -> str:
        string = ""
        max_len = 0
        for s in strs:
            string += s
            # print(Solution.encription)
            # if max_len == len(string):
            #     continue
            # max_len = max(max_len, len(string))
            Solution.encription.append(len(s))
        return string

    def decode(self, s: str) -> List[str]:
        strs = []
        index = 0
        for code in Solution.encription:
            strs.append(s[index: index + code])
            index += code
        # if len(Solution.encription) == 0: return [""]
        Solution.encription = []
        return strs
