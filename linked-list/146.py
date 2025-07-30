# Doubly Linked List
# Hash Map

class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity  # Initialize the maximum capacity of the cache
        self.cache = {} # Initialize a hash map to store key-node pairs
        # left = LRU, right = Most recently used
        self.left, self.right = Node(0), Node(0)  # Create dummy left (LRU) and right (MRU) nodes
        self.left.next, self.right.prev = self.right, self.left  # Connect left and right dummy nodes to each other

    # remove from the list
    def remove(self, node):
        prev, nxt = node.prev, node.next  # Get the previous and next nodes of the node to be removed
        prev.next, nxt.prev = nxt, prev  # Bypass the node by connecting its previous to its next, and vice-versa

    # insert at right(most recently used)
    def insert(self, node):
        prev, nxt = self.right.prev, self.right  # Get the node before the right dummy (current MRU) and the right dummy
        prev.next = nxt.prev = node  # Connect the previous node to the new node, and the new node to the right dummy
        node.next, node.prev = nxt, prev  # Connect the new node to the right dummy and to the previous node

    def get(self, key: int) -> int:
        if key in self.cache:  # Check if the key exists in the cache
            self.remove(self.cache[key])  # Remove the accessed node from its current position in the list
            self.insert(self.cache[key])  # Insert the accessed node at the right (MRU) end of the list
            return self.cache[key].val  # Return the value of the accessed node
        return -1  # Return -1 if the key is not found in the cache
        
    def put(self, key: int, value: int) -> None:
        if key in self.cache:  # Check if the key already exists in the cache
            self.remove(self.cache[key])  # If it exists, remove the old node from the list
        self.cache[key] = Node(key, value)  # Create a new node with the given key and value, and store it in the cache
        self.insert(self.cache[key])  # Insert the new node at the right (MRU) end of the list

        if len(self.cache) > self.cap:  # Check if the cache size exceeds its capacity
            # remove or evict the least recently used from the hash map
            lru = self.left.next  # Get the least recently used node (the one after the left dummy)
            self.remove(lru)  # Remove the LRU node from the list
            del self.cache[lru.key]  # Remove the LRU node from the hash map

# Another approach
# Tc = O(1)
# Sc - O(n)
from collections import OrderedDict
class LRUCache:
    def __init__(self, capacity):
        self.cap = capacity
        self.cache = OrderedDict()
    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key) #move to most recent
        return self.cache[key]
    def put(self, key, value):
        if key in self.cache:
            del self.cache[key]
        elif len(self.cache) >= self.cap:
            self.cache.popitem(last=False) #evict LRU
        self.cache[key] = value #insert new(or updated) key
