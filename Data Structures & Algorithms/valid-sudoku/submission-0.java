class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set <String> seen = new HashSet<>();
        for(int i =0; i<9;i++){
            for(int j=0; j<9 ;j++){
                 char pos= board[i][j];
                 if(pos!='.'){ 
                    if(!seen.add(pos+"in row"+i)||!seen.add(pos+"in coloumn"+j)
                    || !seen.add(pos+","+i/3+"piruuus"+j/3) ) return false;
                  
                 }

            }
        }
     return true;
        
    }
}
