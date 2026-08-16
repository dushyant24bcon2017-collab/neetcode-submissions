# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        #for this question we can haev two pointers one slow and one fast they will start together if the fast poiter reaches the slow pointer iyt is a cycle 
        slow = fast = head
        while fast and fast.next: 
            slow = slow.next
            fast = fast.next.next
            if slow == fast: 
                return True
        return False 

        