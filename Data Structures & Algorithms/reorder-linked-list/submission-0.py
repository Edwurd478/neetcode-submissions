# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        fast = head
        slow = head
        #print("test")
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        #print("found middle")
        while slow:
            #print(slow.val)
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        #print("reversed second half")
        while prev:
            #print(head.val, prev.val)
            tmp = head.next
            othertmp = prev.next
            head.next = prev
            if tmp != prev:
                prev.next = tmp
            head = tmp
            prev = othertmp

             