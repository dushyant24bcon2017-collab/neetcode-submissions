class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indices = dict()
        #Storing all the elements with their indexes
        #when we are doing 2 pass approach we also need to take care 
        #that we are not including the same index twice so we apply
        #cond where we check both of their index are not same 
        # indices[diff]!=i
        for i , n in enumerate(nums):
            indices[n]=i

        for i , n in enumerate(nums):
            diff = target - n 
            if(diff in  nums and indices[diff]!=i):
                return [i,indices[diff]] 
        
        return []
            

        
        

        