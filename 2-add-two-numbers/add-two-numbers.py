# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        stack1 = []
        stack2 = []

        while l1:
            stack1.append(l1.val)
            l1 = l1.next
        
        while l2:
            stack2.append(l2.val)
            l2 = l2.next
        
        s1 = ""
        s2 = ""
        
        while stack1:
            s1 += str(stack1.pop())

        while stack2:
            s2 += str(stack2.pop())

        num = int(s1) + int(s2)
        res = ListNode()
        strNum = str(num)
        strNum = strNum[::-1]
        if num == 0:
            return ListNode(0)
        head = None
        for i in range(len(strNum)):
            newNode = ListNode(int(strNum[i]))
            if not head:
                head = newNode
                curr = head
            else:
                curr.next = newNode
                curr = curr.next
        
        return head
