class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<String> set = new HashSet<>();
        for(int r=0;r<9;r++){
            for(int c=0;c<9;c++){
                int pos =board[r][c];
                if(pos!='.'){
                    if(!set.add(pos+"row"+r) || !set.add(pos+"coloumn"+c) ||!set.add(pos+"pikachu"+r/3+','+c/3)){
                        return false;
                    }
                }
            }
        }
       return true; 
    }
}
