# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if root == None :
            return 0

        if root.left and root.right :
            depth = 1 +  + self.maxDepth(root.right)
            dL = self.maxDepth(root.left)
            dR = self.maxDepth(root.right)
            return max(dR,dL) + 1 

        elif root.left and not root.right :
            depth = 1 + self.maxDepth(root.left)
            return depth

        elif root.right and not root.left : 
            depth = 1 + self.maxDepth(root.right)
            return depth

        else :
             return 1
                             