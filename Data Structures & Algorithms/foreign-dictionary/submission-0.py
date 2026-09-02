class Solution:
    def foreignDictionary(self, words):

        # Create a graph containing every character
        adj = {c: set() for word in words for c in word}

        # Compare adjacent words
        for i in range(len(words) - 1):

            w1 = words[i]
            w2 = words[i + 1]

            minLen = min(len(w1), len(w2))

            # Find the first different character
            for j in range(minLen):

                if w1[j] != w2[j]:

                    # w1[j] comes before w2[j]
                    adj[w1[j]].add(w2[j])

                    # Only the first difference matters
                    break

            # Invalid prefix case
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""

        # 0 = not visited
        # 1 = currently visiting
        # 2 = completely visited
        state = {}

        res = []

        def dfs(c):

            # Already visited
            if c in state:
                return state[c] == 2

            # Mark as currently visiting
            state[c] = 1

            # Visit all neighbors
            for nei in adj[c]:

                if not dfs(nei):
                    return False

            # Finished processing this character
            state[c] = 2

            res.append(c)

            return True

        # Run DFS for every character
        for c in adj:

            if not dfs(c):
                return ""

        # DFS gives reverse topological order
        res.reverse()

        return "".join(res)