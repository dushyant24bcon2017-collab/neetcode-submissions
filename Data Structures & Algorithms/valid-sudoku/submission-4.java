class Solution {
    public boolean isValidSudoku(char[][] board) {
        Set<String> set = new HashSet<>();
        
            for(int i=0 ; i<9;i++){
                for(int j=0 ; j<9; j++){
                    char pos = board[i][j];
                    if(pos!= '.'){ 
                    if(!set.add(pos +"row"+ i )|| !set.add(pos+ "coloumn"+ j ) || !set.add(pos +"square"+ i/3 +"and" +j/3 ) ) return false;
                    }
                }

            }
            return true;
        }
        
        
    }

