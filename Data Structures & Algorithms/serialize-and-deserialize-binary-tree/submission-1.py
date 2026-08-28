# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Codec:

    def serialize(self, root):
        res = []

        def dfs(node):
            # Missing node
            if not node:
                res.append("N")
                return

            # Store current node
            res.append(str(node.val))

            # Store left subtree
            dfs(node.left)

            # Store right subtree
            dfs(node.right)

        dfs(root)

        return ",".join(res)

    def deserialize(self, data):
        vals = data.split(",")
        self.i = 0

        def dfs():
            # Missing node
            if vals[self.i] == "N":
                self.i += 1
                return None

            # Create current node
            node = TreeNode(int(vals[self.i]))
            self.i += 1

            # Build left subtree
            node.left = dfs()

            # Build right subtree
            node.right = dfs()

            return node

        return dfs()