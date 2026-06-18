class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character,Integer> map= new HashMap<>();
        if(s.length()!=t.length()) return false;
         
        for(int i=0 ; i <s.length();i++){
          char  sc=s.charAt(i);
           char tc=t.charAt(i);
            map.put(sc,map.getOrDefault(sc,0)+1);
            map.put(tc,map.getOrDefault(tc,0)-1);
        }
         for(int num: map.values()){
            if(num!=0) return false;
         }
        return true;

    }

}
