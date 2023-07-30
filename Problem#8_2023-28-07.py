""" 
Problem :
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
"""

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
class Solution:
    def count_unival_subtrees(root):
        def is_unival_subtree(node, value):
            if not node:
                return True
            if node.val != value:
                return False
            return is_unival_subtree(node.left, value) and is_unival_subtree(node.right, value)

        def dfs_count_unival_subtrees(node):
            if not node:
                return 0

            total_count = dfs_count_unival_subtrees(node.left) + dfs_count_unival_subtrees(node.right)

            if is_unival_subtree(node.left, node.val) and is_unival_subtree(node.right, node.val):
                total_count += 1

            return total_count

        return dfs_count_unival_subtrees(root)

#__main__
root = TreeNode(0)
root.left = TreeNode(1)
root.right = TreeNode(0)
root.right.left = TreeNode(1)
root.right.right = TreeNode(0)
root.right.left.left = TreeNode(1)
root.right.left.right = TreeNode(1)

print(Solution.count_unival_subtrees(root))  # Output: 5
