class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #here we can see that the the array is sorted in two parts and it 
        #has a piviot point , the piviot point happens to be the minimum
        #element we know how to find the minimum after finding the minium 
        #we can then have three conditions if the array is completely sorted
        # that means min_e = nums[0] right sorted and left sorted and 
        # perform normal bianry search on them 
        min_e =nums[0]
        l,r=0,len(nums)-1
        while l<r:
            m = (l+r)//2
            if nums[m] > nums[r]:
                l = m+1
            else:
                r=m

        min_e = l
        if min_e==0:
            l,r=0,len(nums)-1
        elif target >= nums[0] and target<= nums[min_e-1]:
            l,r= 0,min_e-1
        else :
            l,r=min_e,len(nums)-1
        while l<=r :
            m = (l+r)//2
            if nums[m]==target: 
                return m
            elif nums[m]>target:
                r=m-1
            else:
                l=m+1
        return -1