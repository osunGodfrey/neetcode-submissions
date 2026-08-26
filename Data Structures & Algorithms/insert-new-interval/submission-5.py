class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        # print(intervals)
        for index in range(len(intervals)):
            interval = intervals[index]
            start = interval[0]
            if start > newInterval[0]:
                intervals.insert(index, newInterval)
                break
            else:
                intervals.append(newInterval)
        # print(intervals)

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
                continue
            else:
                last_interval[1] = max(last_interval[1], interval[1])
            merge_interval.append(last_interval)
            # print(interval, merge_interval)
            # print("...")
        return merge_interval
            

        