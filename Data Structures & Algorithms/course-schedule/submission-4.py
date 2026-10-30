from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if len(prerequisites) == 0 and numCourses > 0:
            return True 
            
        res = 0 
        adjList = {i : [] for i in range(numCourses)}
        inDegree = {i : 0 for i in range(numCourses)}
        queue = deque()

        for pair in prerequisites : 
            adjList[pair[1]].append(pair[0])
            inDegree[pair[0]] += 1 


        for vertex in inDegree : 
            if inDegree[vertex] == 0 : 
                queue.append(vertex)

        
        while queue : 
            currVertex = queue.popleft()
            res += 1
            for vertex in adjList[currVertex] :
                inDegree[vertex] -= 1
                if inDegree[vertex] == 0 : 
                    queue.append(vertex)

        
        return res == numCourses

        

            
            
