# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        #brute force 
        sortedlist = []
        for lst in lists:
            while lst:
                sortedlist.append(lst.val)
                lst=lst.next
        sortedlist.sort()
        dummy = ListNode()
        res=dummy
        for elem in sortedlist:
            dummy.next= ListNode(elem)
            dummy = dummy.next
        return res.next
        