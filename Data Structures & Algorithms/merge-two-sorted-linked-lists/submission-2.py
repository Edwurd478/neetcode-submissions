# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr1 = list1
        curr2 = list2
        newHead = ListNode(-101, None)
        curr = newHead
        while curr1 != None or curr2 != None:
            if curr2 != None and (curr1 == None or curr2.val < curr1.val):
                curr.next = curr2
                curr = curr.next
                curr2 = curr2.next
            else:
                curr.next = curr1
                curr = curr.next
                curr1 = curr1.next
        
        """
        while curr1 != None or curr2 != None:
            if curr1 == None:
                while curr2 != None:
                    curr.next = curr2
                    curr = curr.next
                    curr2 = curr2.next
            elif curr2 == None:
                while curr1 != None:
                    curr.next = curr1
                    curr = curr.next
                    curr1 = curr1.next
            else:
                if curr1.val < curr2.val:
                    curr.next = curr1
                    curr = curr.next
                    curr1 = curr1.next
                else:
                    curr.next = curr2
                    curr = curr.next
                    curr2 = curr2.next
        """
        return newHead.next

        