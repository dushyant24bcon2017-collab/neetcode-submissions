class Solution {
    public boolean isAnagram(String s, String t) {
        Map<Character,Integer> map = new HashMap<>();
        int sl= s.length();
        int tl= t.length();
        if(sl!=tl) return false;
        for(int i=0; i<sl;i++){
            map.put(s.charAt(i), map.getOrDefault(s.charAt(i),0)+1);
            map.put(t.charAt(i), map.getOrDefault(t.charAt(i),0)-1);

        }
        for(int c: map.values()){ 
        if(c!=0) return false;

        }
        return true;


    }
}
