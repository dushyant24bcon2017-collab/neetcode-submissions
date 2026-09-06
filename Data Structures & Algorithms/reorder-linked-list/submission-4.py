# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        #TO REORDER LINKED LIST IN THIS MANNER WHAT WE NEED TO DO IS , THAT WE NEED TO UNDERSTANT THAT WE ARE MERGING THE FIRST AND THE SECOND PART OF THGE LIST FOR THAT WE FOR SO FIRST USING THE SLOW AND FAST POINTERS WE NEED TO SEPERATE THE FIRST AND THE SECOND PART OF THE LIST AND AFTER THAT WE NEED TO REVERSE THE SECOND PART OF THE LIST SO THAT WE CAN GET THE ELEMENTS FROM THE LAST PART AFTER THAT WE NEED TO TAKE 1 ELEM FRIOM THE FIRST AND RTHEN ONE FROM SECOND WE ALSO NEED TO HANDLE EDGE CASES LIKE MAKING LAST ELEM OF FIRST LIST POINT TO NULL 
        slow , fast = head , head.next 
        while fast and fast.next:
            slow = slow.next 
            fast = fast.next.next 
        second = slow.next
        slow.next= None 
        prev = None 
        while second: 
            temp = second.next 
            second.next =  prev 
            prev = second 
            second = temp 
        first , second = head , prev 
        while second: 
            temp1 , temp2 = first.next , second.next 
            first.next= second 
            second.next = temp1 
            first , second = temp1 , temp2 
    