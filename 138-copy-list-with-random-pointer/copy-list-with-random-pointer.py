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
        curr = head
        hashMap = {None : None}

        # First iteration 
        while curr:
            copy = Node(curr.val) 
            hashMap[curr] = copy 
            curr = curr.next
        
        # Next iteration
        curr = head
        while curr:
            copy = hashMap[curr]
            copy.random = hashMap[curr.random]
            copy.next = hashMap[curr.next]
            curr = curr.next
        
        return hashMap[head]

        

            