# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        globalList = []
        if root.left == None and root.right == None :
            return root.val 

        def dfs(root) : 
            nonlocal globalList 
            if root is None : 
                return
            
            dfs(root.left) 
            globalList.append(root.val)
            dfs(root.right) 
            

        dfs(root)
        
        return globalList[k - 1] 
