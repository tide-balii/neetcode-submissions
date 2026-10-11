# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if root is None : 
	        return []

        q = deque([root])
        res = []
        level = 0
        counter = -1

        while q : 
            level = len(q)
            counter += 1 
            res.append([]) 
            for i in range (level) : 
                curr = q.popleft()
                res[counter].append(curr.val)
                if curr.left : 
                    q.append(curr.left)
                if curr.right : 
                    q.append(curr.right)
        return res
