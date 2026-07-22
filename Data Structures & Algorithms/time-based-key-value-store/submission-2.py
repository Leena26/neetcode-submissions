class TimeMap:

    def __init__(self):
        self.hashmap = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.hashmap[key].append([timestamp, value])
        

    def get(self, key: str, timestamp: int) -> str:
        arr = self.hashmap[key]
        arr.sort()
        res = [0, 0]
        for i in arr:
            if i[0] <= timestamp and i[0] > res[0]:
                res = i
        if res[0] != 0:
            return str(res[1])
        return ""

        
