class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #here we can do the method of buvket sort but the opposite way forst we can store all the elems with freq then with the help of the list let the index be the freq and the value on that index be the vlaue and in the end we can iterate from end till we reach the freq 
        freq ={}
        bucket=[[] for i in range(len(nums)+1)]
        for n in nums:
            freq[n]= 1 + freq.get(n,0)
        for key, value in freq.items():
            bucket[value].append(key)

        res = []
        for i in range(len(bucket)-1,0,-1):
            for n in bucket[i]:
                res.append(n)
                if len(res)==k:
                    return res
        return -1
                    




























        
        
        