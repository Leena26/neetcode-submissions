# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        rootStr = self.serialise(root)
        subRootStr = self.serialise(subRoot)

        return subRootStr in rootStr

    def serialise(self, node):
        if not node:
            return "X"
        return "#" + str(node.val) + self.serialise(node.left) + self.serialise(node.right)
    
        
        

    
        