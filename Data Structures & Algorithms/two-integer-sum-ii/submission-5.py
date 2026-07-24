class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n = numbers 
        l,r = 0 , len(n)-1
        while l<r:
            if n[l]+n[r]>target:
                r = r-1
            elif n[l]+n[r]<target:
                l = l+1
            else:
                return [l+1,r+1]
        return -1
        