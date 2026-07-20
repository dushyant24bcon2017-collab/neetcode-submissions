class TimeMap:

    def __init__(self):
        # self.keyvalue = {}
        #here to solve this by a brute force way  we can have a dict which store 
        # another dictinary whih has the value ,kind of like 
        #{"apple": {10: ["red"], 20: ["green"]}}
        self.keystore ={}

    def set(self, key: str, value: str, timestamp: int) -> None:
        # if key not in self.keyvalue : 
        #     self.keyvalue[key]={}
        # if timestamp not in self.keyvalue[key]:
        #     self.keyvalue[key][timestamp]=[]
        # self.keyvalue[key][timestamp].append(value)
        if key not in self.keystore:
            self.keystore[key]=[]
        self.keystore[key].append([value,timestamp])

       
    def get(self, key: str, timestamp: int) -> str:
        # if key not in self.keyvalue:
        #     return ""
        # seen =0 # this to count the latest time stamp so
        # #timestamp_prev <= timestamp cond is satisfied 
        # for time in self.keyvalue[key]:
        #     if time<=timestamp:
        #         seen= max(seen, time)
        # if seen == 0:
        #     return 
        # return self.keyvalue[key][seen][0]
        if key not in self.keystore: 
            return ""
        res,value = "" , self.keystore.get(key,[])
        l,r = 0, len(value)-1
        while l<=r :
            m =( l+r)//2
            if value[m][1]<= timestamp:
                res = value[m][0]
                l=m+1
            else:
                r=m-1
        return res 

       
            

      
        
