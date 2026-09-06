# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        # to detect the cycle we can use slow and fast pointer we can make them start both at the same place and then incrementr the slow by one and fast by two if both of them mean then qwe have a cycle and if the dont we dont have cycle 
        slow = fast = head 
        while fast and fast.next:
            slow = slow.next 
            fast= fast.next.next 
            if slow == fast: 
                return True
        return False 
        