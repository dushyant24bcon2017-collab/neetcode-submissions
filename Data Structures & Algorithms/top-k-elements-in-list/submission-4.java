class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer, Integer> map = new HashMap<>();
        List<Integer>[] bucket = new List[nums.length+1];
        for(int i : nums){
            map.put(i, map.getOrDefault(i,0)+1);
        }
        for(int i : map.keySet()){
            int freq = map.get(i);
            if(bucket[freq]== null){
                bucket[freq] = new ArrayList<>();
            }
            bucket[freq].add(i);        
            }
            int [] res = new int[k];
            int index =0;
            for(int i = bucket.length-1; i >0 && index<k ; i--){
                if(bucket[i]!= null){ 
                for(int n : bucket[i]){
                    res[index++]=n;
                    if(index==k){
                        return res;
                    }
                }
            }
            }
            return res;
    }
}
