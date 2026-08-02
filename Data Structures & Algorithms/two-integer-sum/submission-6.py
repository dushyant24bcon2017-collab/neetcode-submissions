class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        elem = dict()
        for i,n in enumerate(nums): 
            tar = target- n 
            if tar in elem:
                return [elem[tar], i]
            elem[n]=i
        return []
            
        
        

        