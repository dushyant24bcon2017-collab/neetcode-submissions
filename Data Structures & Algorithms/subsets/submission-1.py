class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        path = []
        def dfs(val):
            result.append(path[:])
            for i in range(val,len(nums)):
                path.append(nums[i])
                dfs(i+1)
                path.pop()
         
        dfs(0)
        return result