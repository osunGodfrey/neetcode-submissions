class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        max_freq = 0
        freq_hash = {}
        for n in nums:
            max_freq = max(max_freq, freq_hash.get(n, 0) + 1)
            freq_hash[n] = freq_hash.get(n, 0) + 1
    
        kTop_list = []
        for _ in range(max_freq + 1):
            for digit in freq_hash.keys():
                # print(freq_hash)
                if freq_hash[digit] == 0:
                    kTop_list.append(digit)
                freq_hash[digit] = freq_hash[digit] - 1
        return kTop_list[len(kTop_list) - k:]
            

        # k_slider = 0
        # kTop_list = [0] * k
        # kTop_freq = [0] * k #[freq_hash[n]]  + ([0] * (k - 1))
        # first_pass = True
        # print(freq_hash)
        # for digit in freq_hash.keys():
        #     print(kTop_list)
        #     print(digit, freq_hash[digit], k_slider, kTop_freq[k_slider])
        #     if freq_hash[digit] > kTop_freq[k_slider]:
        #         # if first_pass:
        #         #     k_slider = (k_slider + 1) % k
        #         kTop_freq[k_slider] = freq_hash[digit]
        #         kTop_list[k_slider] = digit
        #         # if first_pass:
        #         #     first_pass = False
        #         # else:
        #         #     k_slider = (k_slider + 1) % k
        #         k_slider = (k_slider + 1) % k
        # print(kTop_list)
        # return kTop_list




        