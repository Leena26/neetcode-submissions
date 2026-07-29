# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        def checkTree(x, y):
            if not x or not y:
                return x==None and y==None 
            if x.val != y.val:
                return False
            left = checkTree(x.left, y.left)
            right = checkTree(x.right, y.right)

            return left and right
        return checkTree(p, q)














     










