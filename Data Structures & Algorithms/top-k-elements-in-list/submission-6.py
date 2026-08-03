class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #first we make  a bucket 
        bucket = [ [] for i in range(len(nums)+1)]
        #we make our frequency list 
        freq = {}
        for i in nums : 
            freq[i] = 1 + freq.get(i,0) 
        for key ,value in freq.items():
            bucket[value].append(key)
        res=[]
        for i in range(len(bucket)-1, 0, -1):
            for j in bucket[i]:
                res.append(j)
                if len(res)==k:
                    return res
        return []