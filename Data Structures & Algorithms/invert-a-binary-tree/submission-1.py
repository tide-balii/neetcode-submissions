# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root != None and root.left != None and root.right != None : 
            temp = root.left
            root.left = root.right
            root.right = temp 

            self.invertTree(root.left)
            self.invertTree(root.right)
        

        elif root != None and root.left != None and not root.right : 
            root.right = root.left
            root.left = None 
            self.invertTree(root.right)

        elif root != None and root.right != None and not root.left : 
            root.left = root.right
            root.right = None
            self.invertTree(root.left) 
    
        return root 
        