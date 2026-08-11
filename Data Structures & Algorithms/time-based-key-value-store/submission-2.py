from collections import defaultdict
class TimeMap:

    def __init__(self):
        self.map = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.map[key].append((timestamp, value))

    def get(self, key: str, timestamp: int) -> str:
        search = self.map[key]
        l, r = 0, len(search)-1
        ans = ""

        while l <= r:
            m = (l + r) // 2
            if search[m][0] == timestamp or (m == len(search) - 1 and timestamp > search[m][0]) or (search[m][0] < timestamp and search[m+1][0] > timestamp):
                ans = search[m][1]
                break
            
            if search[m][0] < timestamp:
                l = m + 1
            else:
                r = m - 1

        return ans
