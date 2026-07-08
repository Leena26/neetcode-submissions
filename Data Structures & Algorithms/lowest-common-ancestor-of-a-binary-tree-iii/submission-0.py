"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        if not root or root==p or root==q:
            return root

        pSet = set()
        curr = p
        while curr:
            pSet.add(curr)
            curr = curr.parent
        
        curr = q
        while curr and curr not in pSet:
            curr = curr.parent
        return curr
