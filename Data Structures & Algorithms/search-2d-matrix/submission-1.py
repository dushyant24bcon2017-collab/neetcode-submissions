class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #here each row is in sorted manner in increasing order and the 
        #first integer of every row is greater than last integer of the
        #previous row , this means every row and col is sorted and hence 
        # we can perform a bianry serach first we can bianry searh throgh
        #rows to check the middle row and compare it with the first 
        #and the last element of the row if it is greater or smaller we perform 
        #binary search conditions , for the false cases where the top<=bot 
        #we return false  
        # if they are the crrect range of the target and then 
        #performing bianry search through that rannge 

        ROWS , COLS = len(matrix), len(matrix[0])

        #FOR LOOKING IN ROWS TO FIND THE RANGE 
        top, bot = 0 , ROWS-1 
        while top <= bot :
            tar= (top + bot)//2
            if target > matrix[tar][-1]:
                top = tar + 1 
            elif target < matrix[tar][0]:
                bot = tar -1 
            else : 
                break 
        if top > bot : 
            return False 
        row =  (top + bot)//2 
        l,r = 0 , COLS-1
        while l <= r : 
            tar = (l+r)//2
            if target > matrix[row][tar]:
                l= tar + 1 
            elif target < matrix[row][tar]:
                r= tar -1
            else : 
                return True 
        return False 


            