class TrieNode:
    def __init__(self):
        self.children = {}
        self.endOfWord = False


class WordDictionary:

    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word):
        curr = self.root

        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()

            curr = curr.children[c]

        curr.endOfWord = True

    def search(self, word):
        def dfs(j, node):
            if j == len(word):
                return node.endOfWord

            c = word[j]

            if c == '.':
                for child in node.children.values():
                    if dfs(j + 1, child):
                        return True

                return False

            if c not in node.children:
                return False

            return dfs(j + 1, node.children[c])

        return dfs(0, self.root)