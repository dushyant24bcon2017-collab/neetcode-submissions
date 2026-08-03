class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #WE ARE GIVEN A LIST AND WE NEED TO GROUP ALL THE ANAGRAMS IN THAT 
        #LIST AND THEN RETURN LIST OF ALL THOSE GROUPS 
        #HERE THE LOGIC THAT WE WILL USE IS WE WILL MAKE A ALPHABET
        #ARRRAY OF 26 LETTER WHIHC WILL BE UNIQUE AND WHEN WE WILL GROUP 
        #ALL THE SAME ARRAYS TOGETEHRWE WILL CREATE A HASHMAP WHERE WE WILL
        #MAP THE 26 LETTER ARRRAY TO ALL OUR WORDS WHICH M,ATCH THE SAME 
        #PATTERN WE WILL USE A DEFAULT DICT 
        res = defaultdict(list)
        for s in strs:
            alpha=[0]*26
            for c in s : 
                alpha[ord('a')-ord(c)]+=1
            res[tuple(alpha)].append(s)
        return list(res.values())
        
         

        