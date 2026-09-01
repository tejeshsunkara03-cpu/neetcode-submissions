class Solution:
    def countComponents(self, n, edges):

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()
        components = 0

        def dfs(node):

            if node in visited:
                return

            visited.add(node)

            for neighbor in graph[node]:
                dfs(neighbor)

        for node in range(n):

            if node not in visited:
                components += 1
                dfs(node)

        return components