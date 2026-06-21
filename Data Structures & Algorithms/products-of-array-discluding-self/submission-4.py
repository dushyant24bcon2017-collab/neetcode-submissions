class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prod,zerocnt = 1, 0
        for n in nums: 
            if n:
                prod*=n
            else:
                zerocnt+=1

        if zerocnt>1: return [0]*len(nums)
        res=[1]*len(nums)
        for i , n in enumerate(nums): 
            if zerocnt: res[i]=0 if n else prod
            else:
                res[i]=prod//n

        return res