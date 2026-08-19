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
        #what we can do here is we can leverage a hash map by first storing all the vlaues of the main node in the hash map and creating nodes with values but no wiring for our deep copy and in the second pass we wire them here we  use a pyhton principle When you write copy = oldToCopy[cur], you are not extracting a value out of the hashmap to create a separate local duplicate. You are simply taking your local name tag (copy) and slapping it onto the exact same physical node object that the hashmap is pointing to. so this means we can make chaneges to copy and the chnages will be made to the hashmap  
        oldToCopy = {None:None}
        curr = head
        while curr:
            copy = Node(curr.val)
            oldToCopy[curr]=copy
            curr = curr.next
        curr = head 
        while curr: 
            copy = oldToCopy[curr]
            copy.next=oldToCopy[curr.next]
            copy.random= oldToCopy[curr.random]
            curr= curr.next
        return oldToCopy[head]

        