from collections import deque 
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]: 
        if len(prerequisites) == 0 :
            return [i for i in range(numCourses)]

        addLater = set()
        adjList = {i: [] for i in range(numCourses)} 
        inDegree = {i : 0 for i in range(numCourses)}
        queue = deque()
        coursesTaken = 0 
        res = []

        for pair in prerequisites : 
            adjList[pair[1]].append(pair[0])
            inDegree[pair[0]] += 1 
        

        for vertex in inDegree : 
            if inDegree[vertex] == 0 : 
                queue.append(vertex)
        

        while queue : 
            currVertex = queue.popleft()
            coursesTaken += 1 
            if len(adjList[currVertex]) == 0 :
                addLater.add(currVertex)
                continue
            res.append(currVertex)

            for vertex in adjList[currVertex] : 
                inDegree[vertex] -= 1 
                if inDegree[vertex] == 0 : 
                    queue.append(vertex) 


        if numCourses == coursesTaken : 
            res.extend(addLater)
            return res

        return []


        