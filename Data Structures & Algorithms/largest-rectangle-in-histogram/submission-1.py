class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        #intution we can use a stack here , monotonic stack the trick here is that we can
        #extend forwards and backwards but when we get struck into a bar thats  shorter in 
        # height , we pop it and then we calc the area according to i -index and then the new 
        #rectangle we extend it backwards 
        maxArea = 0 
        stack = [] #index , height 
        for i , h in enumerate(heights):
            start = i 
            while stack and stack[-1][1]>= h:
                index , height = stack.pop()
                maxArea = max(maxArea , height * (i - index))
                start=index#extending backwards 
            stack.append((start,h))

        for i , h in stack:
            maxArea= max(maxArea,h * (len(heights)-i) )# because they have reached till the 
            #end that means they havent found a larger rectangle while extending forward 

        return maxArea
            
