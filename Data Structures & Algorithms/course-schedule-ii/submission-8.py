from collections import deque 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]: 
        if len(prerequisites) == 0 :
            return [i for i in range(numCourses)]

        edgeList = {}
        inDegree = {}
        visited = set()
        queue = deque()
        res = []

        for i in range(numCourses) : 
            edgeList[i] = []
            inDegree[i] = 0 

        for i in prerequisites : 
            edgeList[i[1]].append(i[0])
            inDegree[i[0]] += 1 
        
        for i in inDegree : 
            if inDegree[i] == 0 : 
                queue.append(i) 
        
        while queue : 
            currNode = queue.popleft()
            res.append(currNode)
            visited.add(currNode) 
            for i in edgeList[currNode] :
                inDegree[i] -= 1 
                if inDegree[i] == 0 :
                    queue.append(i)

        for i in inDegree : 
            if i in visited or inDegree[i] != 0 :
                continue 
            res.append(i)

        if len(res) == numCourses : 
            return res
        
        return []
        


        

        


