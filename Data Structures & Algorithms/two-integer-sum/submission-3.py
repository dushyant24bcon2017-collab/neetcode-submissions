class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dicta = dict()
        for i , n in enumerate(nums):
            dicta[n]=i
        for i , n in enumerate(nums):
             tar= target-n 
             if(tar in dicta and dicta[tar]!=i):
                 return [i, dicta[tar]]

        return[]

        