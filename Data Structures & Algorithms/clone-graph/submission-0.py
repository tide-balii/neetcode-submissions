"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors =       neighbors if neighbors is not None else []
"""
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node == None : 
            return None
    
        hashMap = {}
        q = deque([node])

        while q :
            currNode = q.popleft() 
            if currNode not in hashMap :
                hashMap[node] = Node(node.val)
            
            for i in range(len(currNode.neighbors)) :
                vertex = currNode.neighbors[i]
                if vertex not in hashMap :
                    hashMap[vertex] = Node(vertex.val)
                    q.append(vertex)
                
                hashMap[currNode].neighbors.append(hashMap[vertex])
                
                
     
        return hashMap[node]




       
  
