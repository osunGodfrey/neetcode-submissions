"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        intervals = sorted(intervals, key = lambda item: item.start)
        if len(intervals) == 0:
            return True
        last_interval = intervals[0]
        if len(intervals) == 1:
            return True
        current_interval = intervals[1]
        if len(intervals) == 2:
            if last_interval.end <= current_interval.start:
                return True
            else:
                return False
        for next_interval in intervals[2:]:
            if (last_interval.end <= current_interval.start and
            current_interval.end <= next_interval.start):
                print((current_interval.start, current_interval.end))
                last_interval = current_interval
                current_interval = next_interval
                continue
            else:
                print((current_interval.start, current_interval.end))
                return False
        return True


