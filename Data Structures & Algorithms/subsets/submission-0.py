class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        sol , res = [],[]
        n = len(nums)
        def dfs(i):
            if i >=n:
                res.append(sol.copy())
                return 
            # we include element 
            sol.append(nums[i])
            dfs(i+1)

            #we pop the element 
            sol.pop()

            #we skip the element 
            dfs(i+1)
        dfs(0)
        return res



        