class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None

class HashMapSeparateChaining:
    def __init__(self, capacity=10):
        self.capacity = capacity
        self.size = 0
        self.buckets = [None] * capacity

    def _hash(self, key):
        return hash(key) % self.capacity

    def insert(self, key, value):
        index = self._hash(key)
        node = self.buckets[index]
        if node is None:
            self.buckets[index] = Node(key, value)
        else:
            while node:
                if node.key == key:
                    node.value = value
                    return
                if node.next is None:
                    node.next = Node(key, value)
                    break
                node = node.next
        self.size += 1

    def find(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        while node:
            if node.key == key:
                return True
            node = node.next
        return False

    def remove(self, key):
        index = self._hash(key)
        node = self.buckets[index]
        prev = None
        while node:
            if node.key == key:
                if prev:
                    prev.next = node.next
                else:
                    self.buckets[index] = node.next
                self.size -= 1
                return True
            prev = node
            node = node.next
        return False

    def print(self):
        for i in range(self.capacity):
            print(f"Bucket {i}:", end=" ")
            node = self.buckets[i]
            while node:
                print(f"({node.key}: {node.value})", end=" -> ")
                node = node.next
            print("None")
        print("-------------")

hashmap_chain = HashMapSeparateChaining()
hashmap_chain.insert('109', 'SATYA')
hashmap_chain.insert('125', 'SHREYA')

hashmap_chain.print()

hashmap_chain.find("109")

