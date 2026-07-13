class TimeMap:
    def __init__(self):
        self.hashTab = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.hashTab:
            self.hashTab[key] = []
        self.hashTab[key].append((value, timestamp))
        return 

    def get(self, key: str, timestamp: int) -> str:
        if key in self.hashTab:
            arr = self.hashTab[key]
            start, end = 0, len(arr) - 1
            res = ""

            while start <= end:
                mid = start + (end - start)//2

                if arr[mid][1] <= timestamp:
                    res = arr[mid][0]
                    start = mid + 1
                else:
                    end = mid - 1
            return res
        
        return ""


# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)