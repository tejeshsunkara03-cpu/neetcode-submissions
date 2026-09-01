class Solution:
    def findOrder(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        visiting = set()
        completed = set()
        order = []

        def dfs(course):

            if course in visiting:
                return False

            if course in completed:
                return True

            visiting.add(course)

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            visiting.remove(course)
            completed.add(course)

            order.append(course)

            return True

        for course in range(numCourses):

            if not dfs(course):
                return []

        order.reverse()

        return order