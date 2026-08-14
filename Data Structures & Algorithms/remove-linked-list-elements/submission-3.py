# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeElements(self, head: Optional[ListNode], val: int) -> Optional[ListNode]:
        newHead = None
        curr = newHead
        while head:
            if head.val != val:
                if not newHead:
                    newHead = ListNode(head.val)
                    curr = newHead
                else:
                    curr.next = ListNode(head.val)
                    curr = curr.next
            head = head.next
        
        return newHead