class Solution:
    def maxArea(self, heights: List[int]) -> int:
        maximum=0
        l,r= 0,len(heights)-1
        while l<r : 
            area=0
            length = r-l
            if heights[l] < heights[r]:
                area =  length * min(heights[l],heights[r])
                l+=1
            else:
                area =  length * min(heights[l],heights[r])
                r-=1
            maximum=max(maximum,area)


        return maximum
        