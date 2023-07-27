""" 
Problem :
An XOR linked list is a more memory efficient doubly linked list. 
Instead of each node holding next and prev fields, it holds a field named both, 
which is an XOR of the next node and the previous node. Implement an XOR linked list; 
it has an add(element) which adds the element to the end, and a get(index) which returns the node at index.

If using a language that has no pointers (such as Python), 
you can assume you have access to get_pointer and dereference_pointer functions 
that converts between nodes and memory addresses.
"""
class Node:
    def __init__(self, data):
        self.data = data
        self.both = None


class XORLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def add(self, element):
        new_node = Node(element)

        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.both = self.tail
            self.tail.both = id(self.tail) ^ id(new_node)
            self.tail = new_node

    def get(self, index):
        current = self.head
        prev_node_addr = 0

        for i in range(index):
            next_node_addr = prev_node_addr ^ id(current.both)

            if next_node_addr:
                prev_node_addr = id(current)
                current = self.dereference_pointer(next_node_addr)
            else:
                raise IndexError("Index out of range")

        return current
    
    def dereference_pointer(address):
        for obj in gc.get_objects():
            if id(obj) == address:
                return obj

        return None


# Helper function to simulate XOR behavior
def xor(a, b):
    return a ^ b if a and b else a or b


# Example usage:
import gc

xor_linked_list = XORLinkedList()
xor_linked_list.add(10)
xor_linked_list.add(20)
xor_linked_list.add(30)

# Get the node at index 1 (value 20)
node_at_index_1 = xor_linked_list.get(1)
print(node_at_index_1.data)  # Output: 20
