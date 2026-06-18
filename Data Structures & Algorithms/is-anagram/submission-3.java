class Solution {
    public boolean isAnagram(String s, String t) {
        if(s.length()!=t.length())return false;
        Map<Character,Integer> mapS = new HashMap<>();
        Map<Character,Integer> mapt = new HashMap<>();
        for(int i=0 ; i<s.length(); i++ ){
            char st = s.charAt(i);
            char tt = t.charAt(i);
            mapS.put(st, mapS.getOrDefault(st,0)+1);
            mapt.put(tt, mapt.getOrDefault(tt,0)+1);

        }
        return mapt.equals(mapS);

        


        

    }
}
