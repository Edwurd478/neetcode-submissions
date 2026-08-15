# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        savedPrev = None
        savedNext = None
        lNode = head
        rNode = head
        counter = 1
        while counter < left:
            savedPrev = lNode
            lNode = lNode.next
            rNode = rNode.next
            counter += 1
        
        while counter < right:
            rNode = rNode.next
            counter += 1
        savedNext = rNode.next

        #print(lNode.val, rNode.val)

        prev = savedNext
        #print(prev.val)
        for i in range(right-left+1):
            #print(prev.val, lNode.val)
            tmp = lNode.next
            lNode.next = prev
            prev = lNode
            lNode = tmp
            #print(prev.val, lNode.val)
        if savedPrev:
            savedPrev.next = rNode
        else:
            head = rNode
        
        return head
        