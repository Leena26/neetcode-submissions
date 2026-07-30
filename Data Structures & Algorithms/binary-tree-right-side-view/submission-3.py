# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
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
        from collections import deque
        if not root:
            return []
        
        res = []
        q = deque([root])
        while q:
            qLen = len(q)
            for i in range(qLen):
                node = q.popleft()
                if i== qLen-1:
                    res.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)
        return res








            
