# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        #Base Case
        if root == None :
            return 0
        if root.left == None and root.right == None: 
            return 1

        #Recursive Case
        leftDepth = 0 
        rightDepth = 0 
        
        if (root.left != None) :
            leftDepth = self.maxDepth(root.left)
        if (root.right != None) : 
            rightDepth = self.maxDepth(root.right)
        
        depth = max(leftDepth, rightDepth) + 1

        return depth 
 
        