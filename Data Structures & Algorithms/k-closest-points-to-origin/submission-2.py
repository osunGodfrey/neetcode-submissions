class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        queued = []
        heapq.heapify(queued)
        for coord in points:
            coordx, coordy = coord
            # print(coordx)
            distance = math.sqrt(coordx * coordx + coordy * coordy)
            # print(coord)
            # print(distance)
            heapq.heappush(queued, (distance, coord))
            # print(queued)
        result = []
        for _ in range(k):
            result.append(heapq.heappop(queued)[1])
        # print(result)
        return result