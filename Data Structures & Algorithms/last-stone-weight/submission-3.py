class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        last = None;
        while(len(stones) > 0):
            stones.sort()
            # print(stones)
            one = stones.pop()
            # print(one)
            if len(stones) == 0:
                return one
            two = stones.pop()
            # print(two)
            # if len(stones) == 0:
            #     return two
            # print(stones)

            if one == two:
                stones.append(two - one)
            elif one < two:
                stones.append(two - one)
            else:
                stones.append(one - two)
            # print("-//-")
        # return last