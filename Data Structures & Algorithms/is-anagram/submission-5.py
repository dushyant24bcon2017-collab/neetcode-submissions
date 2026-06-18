class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
         sdict , tdict = dict() , dict()
         for i in s : 
             sdict[i]= 1 + sdict.get(i,0)

         for i in t :
             tdict[i] = 1 + tdict.get(i,0)

         if(sdict==tdict):
             return True
        
         return False
        