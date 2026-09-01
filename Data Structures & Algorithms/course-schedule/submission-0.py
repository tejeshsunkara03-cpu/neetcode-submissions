class Solution:
    def canFinish(self, numCourses, prerequisites):

        graph = [[] for _ in range(numCourses)]

        for course, prerequisite in prerequisites:
            graph[prerequisite].append(course)

        visiting = set()

        def dfs(course):

            if course in visiting:
                return False

            if not graph[course]:
                return True

            visiting.add(course)

            for next_course in graph[course]:
                if not dfs(next_course):
                    return False

            visiting.remove(course)

            graph[course] = []

            return True

        for course in range(numCourses):
            if not dfs(course):
                return False

        return True