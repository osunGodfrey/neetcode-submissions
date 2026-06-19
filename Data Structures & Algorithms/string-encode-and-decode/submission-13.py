class Solution:
    encription = []

    def encode(self, strs: List[str]) -> str:
        string = ""
        for s in strs:
            string += s
            Solution.encription.append(len(s))
        return string

    def decode(self, s: str) -> List[str]:
        strs = []
        index = 0
        for code in Solution.encription:
            strs.append(s[index: index + code])
            index += code
        Solution.encription = []
        return strs
