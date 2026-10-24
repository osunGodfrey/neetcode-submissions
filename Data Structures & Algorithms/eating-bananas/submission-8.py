class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        if len(piles) == 1:
            return math.ceil(piles[0] / h)
        max_k = max(piles)
        min_k = 1
        k = round((max_k - min_k) / 2) + min_k
        time = 0
        count = 0
        best_k = max_k
        while(True):
            time = 0
            count += 1
            # print("K:", k, "<", max_k, ",", min_k, ">")
            for p in piles:
                time += math.ceil(p / k)
                # print(time)
            if time <= h:
                best_k = min(best_k, k)
            if (max_k - min_k) < 2:
                break
            if time <= h:
                max_k = k
            else:
                min_k = k
            k = round((max_k - min_k) / 2) + min_k
            # if count == 8:
            #     break
        return best_k


        