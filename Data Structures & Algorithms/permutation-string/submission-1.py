class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1Count , s2Count = [0]*26 , [0]*26
        if len(s1) > len(s2):
            return False 
        #WE FILL OUR INITIAL ARRAY OF S1 TO COMPARE 
        for i in range(len(s1)):
            s1Count[ord(s1[i])-ord('a')] += 1 
        
        for i in range(0,len(s2)):
            s2Count[ord(s2[i]) - ord('a')] += 1
            
            
            if i >= len(s1): 
                s2Count[ord(s2[i - len(s1)]) - ord('a')] -= 1
                
           
            if s1Count == s2Count:
                return True
                
        
        return False



        


        