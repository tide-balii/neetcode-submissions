# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

from collections import deque 
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if root is None: 
            return []

        queue = deque([root])
        res = []
        level = 0 
        curr = root

        while queue : 
            level = len(queue)
            for i in range(level) :
                curr = queue.popleft()
                if i == 0 :
                    res.append(curr.val)
                if curr.right :
                    queue.append(curr.right)
                if curr.left : 
                    queue.append(curr.left)
        
        return res