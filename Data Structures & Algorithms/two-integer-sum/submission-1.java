class Solution {
    public int[] twoSum(int[] nums, int target) {
        Map<Integer,Integer> map= new HashMap<>();
        for(int i=0;i<nums.length;i++){
        map.put(nums[i],i);
        }
        for(int i = 0; i < nums.length; i++ ){
      
            int tar= target - nums[i];
            if(map.containsKey(tar) && map.get(tar)!=i)  return new int[]{i, map.get(tar)};
        }
        return new int[0] ;
        
    }
}
