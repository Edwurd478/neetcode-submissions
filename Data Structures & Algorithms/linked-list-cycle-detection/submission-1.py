# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        counter = 0
        curr = head
        while curr != None:
            if counter > 1000:
                return True
            curr = curr.next
            counter += 1
        
        return False