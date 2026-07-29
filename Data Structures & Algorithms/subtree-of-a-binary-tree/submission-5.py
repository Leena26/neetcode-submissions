# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootS = self.serialize(root)
        subS = self.serialize(subRoot)
        return subS in rootS
        
    def serialize(self, node):
        if not node:
            return "X"
        
        return "#" + str(node.val) + self.serialize(node.left) + self.serialize(node.right)
        

    
        