class Solution:
    def validTree(self, n, edges):

        if len(edges) != n - 1:
            return False

        graph = [[] for _ in range(n)]

        for a, b in edges:
            graph[a].append(b)
            graph[b].append(a)

        visited = set()

        def dfs(node, parent):

            if node in visited:
                return False

            visited.add(node)

            for neighbor in graph[node]:

                if neighbor == parent:
                    continue

                if not dfs(neighbor, node):
                    return False

            return True

        return len(visited) == n if dfs(0, -1) else False