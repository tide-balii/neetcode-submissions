# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:

        #Base Case 
        if root == None or (root.left == None and root.right == None) : 
            return root

        #Recursive Call
        temp = root.right 
        root.right = root.left
        root.left = temp
        
        if (root.right != None) :
            self.invertTree(root.right)
        if (root.left != None) : 
            self.invertTree(root.left)

        return root
            