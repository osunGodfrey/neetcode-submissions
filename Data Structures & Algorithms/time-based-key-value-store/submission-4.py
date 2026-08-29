import bisect
class TimeMap:

    def __init__(self):
        self.time_map = {}
        

    def set(self, key: str, value: str, timestamp: int) -> None:
        # print("set")
        if key not in self.time_map:
            self.time_map[key] = [(value, timestamp)]
        else:
            # print("search")
            index = bisect.bisect_left(self.time_map[key], timestamp,
            key = lambda x: x[1])
            if (index < len(self.time_map[key]) 
            and self.time_map[key][index][1] == timestamp):
                self.time_map[key][index] = (value, timestamp)
            else:
                bisect.insort(self.time_map[key],
                (value, timestamp),
                key = lambda x: x[1]
                )
        # print(self.time_map)
        
        

    def get(self, key: str, timestamp: int) -> str:
        if key in self.time_map:
            index = bisect.bisect_left(self.time_map[key], timestamp,
            key = lambda x: x[1])
            # print(index - 1)
            if (index < len(self.time_map[key]) 
            and self.time_map[key][index][1] == timestamp):
                return self.time_map[key][index][0]
            elif index - 1 > -1 :
                return self.time_map[key][index - 1][0]
            else:
                if self.time_map[key][-1][1] <= timestamp:
                    return self.time_map[key][-1][0]
        return ""
                
        # print(self.time_map)

        
