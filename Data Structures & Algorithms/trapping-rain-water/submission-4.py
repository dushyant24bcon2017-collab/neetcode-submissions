class Solution:
    def trap(self, height: List[int]) -> int:
        #so here we can perform two pointer approach we can see that for every 
        #bar , the water trapped is the minimmum of the maximumright bar and 
        #maximum left bar minus the height of the bar it self , we also need to 
        #when there will be no bar at the ;eft or right we will update it 
        l,r =0 , len(height)-1
        rightMax , leftMax = height[r],height[l]
        res= 0
        while l<r : 
            if leftMax < rightMax : 
                l+=1
                leftMax = max(leftMax , height[l])
                res+=leftMax-height[l]
            else : 
                r-=1
                rightMax = max(rightMax, height[r])
                res+=rightMax-height[r]
        return res