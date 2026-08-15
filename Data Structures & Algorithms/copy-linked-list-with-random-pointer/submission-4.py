"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
from collections import defaultdict
class Solution:
    def buildList(self, origNode, currNode):
        if origNode.next:
            if origNode.next in self.nodes:
                currNode.next = self.nodex[origNode.next]
            else:
                currNode.next = Node(origNode.next.val)
                self.nodes[origNode.next] = currNode.next
                self.buildList(origNode.next, currNode.next)
        if origNode.random:
            if origNode.random in self.nodes:
                currNode.random = self.nodes[origNode.random]
            else:
                currNode.random = Node(origNode.random.val)
                self.nodes[origNode.random] = currNode.random
                self.buildList(origNode.random, currNode.random)
        
    
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None
        self.head = head
        self.newList = Node(head.val)
        self.nodes = defaultdict(Node)

        self.nodes[self.head] = self.newList
        self.buildList(self.head, self.newList)
        return self.newList