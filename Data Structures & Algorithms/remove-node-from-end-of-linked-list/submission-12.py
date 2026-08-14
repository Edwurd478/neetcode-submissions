# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        length = 0
        curr = head
        while curr:
            length += 1
            curr = curr.next
        
        curr = head
        prev = None
        for i in range(length - n):
            prev = curr
            curr = curr.next
        
        if not prev:
            head = head.next
        else:
            prev.next = curr.next
        
        return head
        
        
        
        

        