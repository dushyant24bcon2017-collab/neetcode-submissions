class Solution {
    public List<List<String>> groupAnagrams(String[] strs) {
        Map<String ,List<String>> map = new HashMap<>();
        for(String s : strs){
         int [] niggermotherfucker = new int [25];
         for(char c : s.toCharArray()){
            niggermotherfucker[c-'a']++;
         }   
         String key= Arrays.toString(niggermotherfucker);
         map.computeIfAbsent(key,k-> new ArrayList<>()).add(s);
        }
        return new ArrayList<>(map.values());
    }
}
