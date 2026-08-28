class TrieNode:
    def __init__(self):
        self.children = {}
        self.isWord = False


class Solution:
    def findWords(self, board, words):
        root = TrieNode()

        # Build Trie
        for word in words:
            curr = root

            for char in word:
                if char not in curr.children:
                    curr.children[char] = TrieNode()

                curr = curr.children[char]

            curr.isWord = True

        ROWS, COLS = len(board), len(board[0])
        res = []

        def dfs(r, c, node, word):

            # Invalid position or character not in Trie
            if (
                r < 0 or c < 0 or
                r >= ROWS or c >= COLS or
                board[r][c] not in node.children
            ):
                return

            # Save the character
            char = board[r][c]

            # Move into Trie
            node = node.children[char]

            # Add character to current word
            word += char

            # Found a complete word
            if node.isWord:
                res.append(word)
                node.isWord = False

            # Mark cell as visited
            board[r][c] = "#"

            # Explore four directions
            dfs(r + 1, c, node, word)
            dfs(r - 1, c, node, word)
            dfs(r, c + 1, node, word)
            dfs(r, c - 1, node, word)

            # Backtrack: restore original character
            board[r][c] = char

        # Start DFS from every cell
        for r in range(ROWS):
            for c in range(COLS):
                dfs(r, c, root, "")

        return res
