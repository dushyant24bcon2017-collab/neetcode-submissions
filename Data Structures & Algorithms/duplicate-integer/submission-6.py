class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seta=set()
        for i in nums:
            if(i in seta):
                return True 
            seta.add(i)
        return False 

        

        