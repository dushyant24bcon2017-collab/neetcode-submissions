class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #the logic we will use here is that if the frequency of letters
        #in both the strings are same then we will return true 
        elemInS=dict()
        elemInT=dict()
        for i in s :
            elemInS[i]=1+elemInS.get(i,0)
        for i in t:
            elemInT[i] = 1 + elemInT.get(i,0)
        if elemInS == elemInT:
            return True
        return False
            
        