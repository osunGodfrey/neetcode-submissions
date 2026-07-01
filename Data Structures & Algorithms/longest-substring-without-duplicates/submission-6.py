class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        substring = set()
        i = 0
        j = 0
        max_length = 0
        while(i < len(s)):
            if s[i] in substring:
                while(j <= i):
                    if s[i] not in substring:
                        break
                    substring.remove(s[j])
                    j += 1
            substring.add(s[i])
            max_length = max(max_length, len(substring))
            i += 1
            # print(substring)
            # print(s[j:i])
        return max_length



        # max_length = 1
        # start_index, last_index = 0, 0
        # for index, string in enumerate(s, start = 0):
        #     if s[last_index] == s[index]:
        #         start_index = index - 1
        #     elif s[start_index] == s[index]:
        #         start_index += 1
        #     last_index = index
        #     max_length = max(max_length, len(s[start_index: last_index]))
        #     print(start_index, last_index, max_length, s[start_index: last_index])
        # return max_length



        