# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        ptr1 = headA
        ptr2 = headB
        flag1 = True
        flag2 = True

        while (ptr1 or flag1) and (ptr2 or flag2):
            if ptr1 and ptr2 and ptr1 == ptr2:
                return ptr1
            
            if not ptr1:
                ptr1 = headB
                flag1 = False
            else:
                ptr1 = ptr1.next
            
            if not ptr2:
                ptr2 = headA
                flag2 = False
            else:
                ptr2 = ptr2.next
        
        return None
            
            