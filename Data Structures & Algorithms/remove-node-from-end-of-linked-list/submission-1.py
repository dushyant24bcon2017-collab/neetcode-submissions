# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        #ofc when we look at the problem first the intution is to reverse the linked list and then do a straight forward approach but we can also use 2 pointers here by making two pointers one left and one rght we initialize the left pointer on the head and right pointer exactly 2 pointers next to it and when the right pointer exhausts our left will be sitting at the node we ant to remoe bu twe wnat to remove thta so we would initialize the left one pointer before the head it would be a dummy pointer 
        right = head 
        dummy = ListNode(0,head)
        left = dummy
        while n>0 and right : 
            right = right.next 
            n-=1
        while right: 
            left=left.next
            right=right.next

        left.next=left.next.next
        return dummy.next
        