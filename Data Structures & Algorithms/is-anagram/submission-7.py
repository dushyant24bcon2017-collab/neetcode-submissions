class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        strsS = {}
        strsT = {}
        for i in s:
            strsS[i]=1 + strsS.get(i,0)
        for i in t: 
            strsT[i]= 1 + strsT.get(i,0)
        if strsS==strsT:
            return True
        return False 
        
        