class Solution {
    public int characterReplacement(String s, int k) {
        // Map ki jagah simple array (A-Z ke liye 26 dabbe)
        int[] arr = new int[26];
        int res = 0;
        int maxf = 0;
        int l = 0;

        for (int r = 0; r < s.length(); r++) {
            // Map.put ki jagah direct index access
            // 'A' - 'A' = 0, 'B' - 'A' = 1...
            arr[s.charAt(r) - 'A']++;
            
            // Max Frequency update
            maxf = Math.max(maxf, arr[s.charAt(r) - 'A']);

            // Shrink logic (Same as before)
            while ((r - l + 1) - maxf > k) {
                arr[s.charAt(l) - 'A']--;
                l++;
            }

            res = Math.max(res, r - l + 1);
        }
        return res;
    }
}