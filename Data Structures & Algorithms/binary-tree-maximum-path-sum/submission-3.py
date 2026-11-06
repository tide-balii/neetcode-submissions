# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        maxLength = float("-inf")
        def dfs(root) -> int : 
            nonlocal maxLength 

            if not root :
                return 0 
            if root and not root.right and not root.left : 
                maxLength = max(root.val, maxLength)
                if root.val >= 0 : 
                    return root.val
                return 0 

        
            LST = dfs(root.left)
            RST = dfs(root.right) 


            maxLength = max(maxLength, LST + RST + root.val)
            maxLength = max(maxLength, root.val)

            if LST < 0 and RST > 0 : 
                if RST + root.val > 0 : 
                    return RST + root.val
                return 0

            if RST < 0 and LST > 0 : 
                if LST + root.val > 0 :
                    return LST + root.val

                return 0

            else :
                if max(LST + root.val, RST + root.val) < 0 :
                    return 0 
                else :
                    return max(LST + root.val, RST + root.val)  

        dfs(root)
        return maxLength