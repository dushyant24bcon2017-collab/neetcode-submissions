class Solution {
    public int[] topKFrequent(int[] nums, int k) {
       Map<Integer,Integer> map = new HashMap<>();
       List <Integer> [] list = new List[nums.length+1];
       for(int n: nums ){
        map.put(n,map.getOrDefault(n,0)+1);
       }

    for(int key: map.keySet()){
        int frequency= map.get(key);
        if(list[frequency]==null){
            list[frequency]= new ArrayList<>();
        }
        list[frequency].add(key);
    }
     int count=0;
     int [] res= new int [k];
     for(int pos=list.length-1; pos>=0 && count<k; pos--){
        if(list[pos]!=null){
            for(int integer: list[pos]){
                res[count++]= integer;
            }

        }
     }

      return res;  
    }
}
