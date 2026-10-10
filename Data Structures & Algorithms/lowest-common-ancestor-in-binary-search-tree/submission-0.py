# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        def dfs(curr, missingNode, path) -> List :
            path.append(curr)
            if curr == missingNode :
                return path
            
            if missingNode.val < curr.val :
                dfs(curr.left, missingNode, path)
            else :
                dfs(curr.right, missingNode, path)
            
            return path
        
        pathofP = []
        pathofQ = []
        pathofP = dfs(root, p, pathofP) 
        pathofQ = dfs(root, q, pathofQ)
        length = min(len(pathofP), len(pathofQ))
        LCA = 0 

        for i in range(length) :
            if pathofP[i] == pathofQ[i] :
                LCA = pathofP[i]
        return LCA
	


        



        