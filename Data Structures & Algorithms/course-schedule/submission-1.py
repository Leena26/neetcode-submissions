class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        
        for c, p in prerequisites:
            graph[c].append(p)
        
        visited = set()
        path = set()

        def dfs(c):
            if c in path:
                return False
            if c in visited:
                return True

            path.add(c)
            for i in graph[c]:
                if not dfs(i):
                    return False
            path.remove(c)
            visited.add(c)
            
            return True
        
        for c in range(numCourses):
            if not dfs(c):
                return False
        return True