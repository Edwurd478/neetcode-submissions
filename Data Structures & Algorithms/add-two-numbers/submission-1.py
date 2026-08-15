# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        sum = None
        curr = sum
        carry = 0
        while l1 or l2:
            if l1 and l2:
                digSum = (l1.val + l2.val + carry)
            elif l1:
                digSum = l1.val + carry
            elif l2:
                digSum = l2.val + carry
            
            if not sum:
                sum = ListNode(digSum % 10)
                curr = sum
            else:
                curr.next = ListNode(digSum % 10)
                curr = curr.next
            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next
            carry = 1 if digSum > 9 else 0
        
        if carry == 1:
            curr.next = ListNode(1)
        return sum
