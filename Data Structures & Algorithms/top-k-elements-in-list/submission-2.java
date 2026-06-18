class Solution {
    public int[] topKFrequent(int[] nums, int k) {
        Map<Integer,Integer> map = new HashMap<>();
        List<Integer>[] list= new List[nums.length+1];
        for(int n : nums){
            map.put(n,map.getOrDefault(n,0)+1);
        }
        for(int n: map.keySet()){
            int i = map.get(n);
            if(list[i]==null){
                list[i]= new ArrayList<>();

            }
            list[i].add(n);
        }
        int [] res= new int[k];
        int count= 0;
        for(int i = nums.length;i>=0 && count<k; i--){
            if(list[i]!=null){
                for(int n : list[i]){
                    res[count]=n;
                    count++;
                }
            }
        } 
            return res;
    
        
    }
}
