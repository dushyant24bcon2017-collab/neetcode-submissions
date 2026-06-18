class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<String>set = new HashSet<>();
        for(int i=0;i<9;i++){
            for(int j=0; j<9;j++){
                int pos= board[i][j];
                if(pos!='.'){
                    if(!set.add(pos+"row"+i )||!set.add(pos+"coloumn"+j)|| !set.add(pos+"small array"+i/3+","+j/3)){
                        return false;
                    }
                }
            }
        }
      return true;  
    }
}
