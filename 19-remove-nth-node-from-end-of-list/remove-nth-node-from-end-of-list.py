# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        dummy = ListNode(0)
        dummy.next = head
        lnode = dummy
        rnode = dummy

        for i in range(n):
            rnode = rnode.next

        while rnode.next is not None:
            rnode = rnode.next
            lnode = lnode.next

 
        
        lnode.next = lnode.next.next

        return dummy.next

