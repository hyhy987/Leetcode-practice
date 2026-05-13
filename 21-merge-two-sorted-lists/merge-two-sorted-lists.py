# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeTwoLists(self, list1, list2):
        p1, p2 = list1, list2
        newList = ListNode()
        curr = newList

        while p1 and p2:
            if p1.val <= p2.val:
                curr.next = p1
                p1 = p1.next
                curr = curr.next
            else:
                curr.next = p2
                p2 = p2.next
                curr = curr.next
        if p1:
            curr.next = p1
        if p2:
            curr.next = p2
        return newList.next
