# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        if root and not root.right and not root.left : 
            return True 
        
        def dfs(node, lowest, highest) : 
            if not node :
                return True
            
            if not (lowest < node.val < highest) : 
                return False


            return dfs(node.left, lowest, node.val) and dfs(node.right, node.val, highest)


        return dfs(root, float("-inf"), float("inf"))