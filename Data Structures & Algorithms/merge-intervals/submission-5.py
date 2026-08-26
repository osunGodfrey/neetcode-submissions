class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda item: item[0])
        merge_interval = []
        for index in range(len(intervals)):
            interval = intervals[index]
            # print(interval, merge_interval)
            if len(merge_interval) == 0:
                merge_interval.append(interval)
                continue
            last_interval = merge_interval.pop()
            if last_interval[1] < interval[0]:
                merge_interval.append(last_interval)
                merge_interval.append(interval)
            else:
                last_interval[1] = max(last_interval[1], interval[1])
                last_interval[0] = min(last_interval[0], interval[0])
                merge_interval.append(last_interval)
            # print(interval, merge_interval)
            # print("...")
        return merge_interval
            

        