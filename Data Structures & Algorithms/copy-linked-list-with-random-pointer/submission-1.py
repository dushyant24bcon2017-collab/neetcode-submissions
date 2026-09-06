"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #HERE WE NEED TO CREATE A DEEP COPY OF THE LINKED LIST WE CAN DO IT BY CAPTURING ALL THE ELEMENTS IN THE HASHMAP WERE WE HKEEP THE VALUE AS A NEW  AND THE WHOLE NODE AS KEY WE JUST WANT TO STORE 
        maph = {None:None}
        dummy = head 
        while dummy:
            maph[dummy] = Node(dummy.val)
            dummy = dummy.next
        dummy = head 
        while dummy: 
            copy=maph[dummy]
            copy.next=maph[dummy.next]
            copy.random = maph[dummy.random]
            dummy = dummy.next
        return maph[head]

        