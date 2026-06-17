class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        alphanums = set("abcdefghijklmnopqrstuvwxyz0987654321")
        alphanums_s = ""
        for letter in s:
            if letter in alphanums:
                alphanums_s = alphanums_s + letter
        flip_s = ""
        for letter in s:
            if letter in alphanums:
                flip_s = letter + flip_s
        # print(flip_s)
        return flip_s == alphanums_s
        