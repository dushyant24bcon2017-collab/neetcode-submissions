class TimeMap:

    def __init__(self):
        self.keyvalue={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyvalue:
            self.keyvalue[key]=[]
        self.keyvalue[key].append([value, timestamp])
    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyvalue: 
            return ""
        res, value = "",self.keyvalue[key]
        l,r = 0, len(value)-1
        while l <= r:
            mid = (l+r)//2
            if value[mid][1]<= timestamp:
                res = value[mid][0]
                l=mid+1
            else: 
                r = mid-1 
        return res 
            

            

        
        
