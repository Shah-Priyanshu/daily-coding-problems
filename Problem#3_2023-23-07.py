"""
Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class

class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
The following test should pass:

node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
"""
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def serialize(root):
        if not root:
            return "None"

        queue = [root]
        serialized = []

        while queue:
            node = queue.pop(0)
            if node:
                serialized.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                serialized.append("None")

        return ",".join(serialized)

    def deserialize(data):
        data = data.split(",")
        root_val = data.pop(0)
        root = Solution.create_node(root_val)
        queue = [root]

        while queue and data:
            node = queue.pop(0)
            left_val = data.pop(0)
            right_val = data.pop(0)

            node.left = Solution.create_node(left_val)
            node.right = Solution.create_node(right_val)

            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

        return root

    def create_node(val):
        if val == "None":
            return None
        return Node(val)

# Test the implementation
node = Node('root', Node('left', Node('left.left')), Node('right'))
serialized_data = Solution.serialize(node)
deserialized_node = Solution.deserialize(serialized_data)

assert deserialized_node.left.left.val == 'left.left'
print("Test passed!")
