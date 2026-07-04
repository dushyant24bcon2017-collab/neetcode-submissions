class Solution:
    def minWindow(self, s: str, t: str) -> str:
        countT , window = dict(), dict() 

        for i in range(len(t)): 
            countT[t[i]] = 1+ countT.get(t[i],0)

        l = 0 
        res,resLen=[-1,-1],float("infinity")
        have , want = 0 , len(countT)
        for i in range(len(s)):
            window[s[i]] = 1 + window.get(s[i], 0)

            if s[i] in countT and window[s[i]] == countT[s[i]]:
                have+= 1 

            while have == want: 
                if i-l+1 < resLen: 
                    res = [l,i]
                    resLen = i-l+1

                window[s[l]]-=1
                if s[l] in countT and window[s[l]]< countT[s[l]] : 
                    have -=1
                l+=1
        
        return s[res[0]:res[1]+1]if resLen!=float("infinity") else  ""

        