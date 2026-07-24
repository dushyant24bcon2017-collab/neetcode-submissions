class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        res=list()
        for i , n in enumerate(nums):
            #we need to take care of these two edge cases that if the 
            #fixed number ever gets bigger than 0 the array is sorted 
            #so we cannot find new pairs and if we find the same fixed
            #number in the outer loop we need to skip that too 
            if n > 0 :
                break
            if i >0 and nums[i]==nums[i-1]:
                continue 
            l,r= i+1 , len(nums)-1
            while l<r:
                #all of this is basically two sum with one fixed value 
                tar = n + nums[l] + nums[r]
                if tar > 0 :
                    r-=1
                elif tar < 0 : 
                    l+=1
                else :
                    res.append([n,nums[l],nums[r]])
                    #after finding the correct pair we update the pointers 
                    #we cn update both the pointer but as we can see that 
                    #when we update one pointer the result changes and when 
                    #while loop would restart we would automatically update 
                    #the other one 
                    l+=1
                    #same goes for this while loop thos is for checkng duplicates 
                    #inside the second loop  
                    while l<r and nums[l]==nums[l-1]:
                        l+=1 
        return res