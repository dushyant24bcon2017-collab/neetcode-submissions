# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # we want to merge the first half and the second half with alternating values 0 , n-1 but when we talk about the second half the values are from end so we can also reverse the linked listand then first take the elem from the first and the second 
        #because we want the first and the second half seerate we will use the slow and fast pointer approach we will initialize slow on the head and faston head.next and slow will move one step at a time and fast will move 2 we willl make the loop till fast and fast.next and the point where slow will end the next to it we will consider it the secod half 
        slow = head 
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast= fast.next.next
        second = slow.next
        slow.next = None
        prev = None
        while second: 
            temp = second.next
            second.next = prev 
            prev = second 
            second = temp 
        second , first = prev , head 
        while second:
            temp1 , temp2 = first.next , second.next 
            first.next =second 
            second.next= temp1
            first,second = temp1 , temp2
            

        