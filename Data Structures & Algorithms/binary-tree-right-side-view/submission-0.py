# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        
        '''
        - for each level get the right most value
        - use breadth first search
            - queue initialised to root
            - res array to store result

        - check right most val at queue
        - for each level enqueue the left and right values in order
        - identify right most vl and appen to res
        - add left val's children, add right val's pointer

        recursion
        - base case: left and right have no children


        '''
        q = collections.deque([root])
        res = []

        while q:
            right = None
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if node:
                    right = node
                    q.append(node.left)
                    q.append(node.right)
            
            if right:
                res.append(right.val)
        
        return res








            
