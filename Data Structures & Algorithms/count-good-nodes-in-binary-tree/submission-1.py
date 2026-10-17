# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        goodNodes = 1 
        maxSeen = root.val 
        def dfs(child, maxSeen) : 
            if child is None : 
                return None
            
            if child.val >= maxSeen : 
                nonlocal goodNodes
                goodNodes += 1 
                maxSeen = child.val 
            
            dfs(child.left, maxSeen)
            return dfs(child.right, maxSeen)

        
        dfs(root.left, maxSeen)
        dfs(root.right,maxSeen)    


        return goodNodes