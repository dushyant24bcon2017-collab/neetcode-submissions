class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq= dict()
        bucket = [[] for i in range(len(nums)+1)]
        for n in nums:
            freq[n]= 1 + freq.get(n,0)

        for num , f in freq.items():
            bucket[f].append(num)

        res=[]
        for i in range (len(bucket)-1, 0 , -1): 
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res


                


         

        




