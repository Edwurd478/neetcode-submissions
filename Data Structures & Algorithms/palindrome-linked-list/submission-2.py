# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        fast = head
        slow = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        prev = None
        while slow:
            tmp = slow.next
            slow.next = prev
            prev = slow
            slow = tmp
        
        while head and prev:
            if head.val != prev.val:
                return False
            head = head.next
            prev = prev.next
        
        return True
        
        """
        newList = copy.deepcopy(head)
        prev = None
        curr = newList
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        curr = head
        while prev and curr:
            if prev.val != curr.val:
                return False
            prev = prev.next
            curr = curr.next
        
        return True
        """