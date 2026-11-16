class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        path = []
        def dfs(start, remaning):
            if remaning == 0:
                res.append(path[:])
                return
            for i in range(start, len(nums)):
                if nums[i]>remaning:
                    continue 
                path.append(nums[i])
                dfs(i,remaning-nums[i])
                path.pop()
        dfs(0,target)
        return res



