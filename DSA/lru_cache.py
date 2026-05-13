class ListNode:
    def __init__(self,key=None, val= None, next = None, prev = None):
        self.key = key
        self.val = val
        self.next = next
        self.prev = prev

class LRUCache:
    
    def __init__(self, capacity: int):
        self.capacity = capacity  # required for the cache to know when to evict the least recently used item
        self.cache = {}
        self.head = ListNode()
        self.tail = ListNode()
        self.head.next = self.tail
        self.tail.prev = self.head
    
    def insert_to_right(self, node):
        prev_node = self.tail.prev
        prev_node.next = node
        node.prev = prev_node
        node.next = self.tail
        self.tail.prev = node
        

    def remove(self,node):
        prev_node = node.prev
        next_node = node.next
        prev_node.next = next_node
        next_node.prev = prev_node

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.remove(node)
        self.insert_to_right(node)
        return node.val

    def put(self,key,value):
        
        if key in self.cache:
            self.remove(self.cahche[key])
        
        node = ListNode(key, value)
        self.cache[key] = node
        self.insert_to_right(node)
            
        if len(self.cache) > self.capacity:
            lru_node = self.head.next
            self.remove(lru_node)
            del self.cache[lru_node.key]


if __name__ == "__main__":
    
    lru = LRUCache(2)
    lru.put(1, 1)  # Cache is {1=1}
    lru.put(2, 2)  # Cache is {1=1, 2=2}
    print(lru.get(1))  # Returns 1
    lru.put(3, 3)  # Evicts key 2, Cache is {1=1, 3=3}
    print(lru.get(2))  # Returns -1 (not found)
    lru.put(4, 4)  # Evicts key 1, Cache is {4=4, 3=3}
    print(lru.get(1))  # Returns -1 (not found)
    print(lru.get(3))  # Returns 3
    print(lru.get(4))  # Returns 4

    