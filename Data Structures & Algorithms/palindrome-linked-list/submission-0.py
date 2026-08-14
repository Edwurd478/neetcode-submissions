# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import copy
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        newList = copy.deepcopy(head)
        prev = None
        curr = newList
        while curr != None:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        curr = head
        while prev != None and curr != None:
            if prev.val != curr.val:
                return False
            prev = prev.next
            curr = curr.next
        
        return True
            