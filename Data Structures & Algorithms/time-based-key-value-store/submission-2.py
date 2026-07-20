class TimeMap:

    def __init__(self):
        self.keyvalue = {}
        #here to solve this by a brute force way  we can have a dict which store 
        # another dictinary whih has the value ,kind of like 
        #{"apple": {10: ["red"], 20: ["green"]}}

    def set(self, key: str, value: str, timestamp: int) -> None:
        if key not in self.keyvalue : 
            self.keyvalue[key]={}
        if timestamp not in self.keyvalue: 
            self.keyvalue[key][timestamp]= []
        self.keyvalue[key][timestamp].append(value)
        

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.keyvalue : 
            return ""
        seen = 0 
        for time in self.keyvalue[key]:
            if time <= timestamp:
                seen = max(seen,time)
            if seen == 0:
                return ""
            

        return self.keyvalue[key][seen][-1]
        
