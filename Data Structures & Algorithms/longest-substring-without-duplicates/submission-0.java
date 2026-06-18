class Solution {
    public int lengthOfLongestSubstring(String s) {
        int i =0 , r = 0;
        int res =0;
        Set<Character> set = new HashSet<>();
        while(r<s.length()){
            if(set.add(s.charAt(r))){
                r++;
                res =Math.max(res,set.size());
            }
            else{
               set.remove(s.charAt(i));
                i++;
            }
          
        }
        return res;
    }
}
