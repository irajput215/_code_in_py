class ListNode:
    def __init__(self, key=None, val = None, next = None):
        self.key = key
        self.val = val
        self.next = next

class MyHashMap:

    def __init__(self):
        self.size = 1000
        self.hashmap = [ListNode() for _ in range(self.size)]
    
    def _hash_function(self, key):
        return key % self.size
    
    def put(self, key: int, value: int) -> None:
        curr = self.hashmap[self._hash_function(key)]
        while curr.next:
            if curr.next.key == key:
                curr.next.val = value
                return 
            curr = curr.next
        curr.next = ListNode(key, value)

    
    def get(self, key: int) -> int:
        curr = self.hashmap[self._hash_function(key)]
        while curr:
            if curr.key == key:
                return curr.val
            curr = curr.next
        return -1

    def remove(self, key: int) -> None:
        index = key % self.size
        curr = self.hashmap[index]
        while curr.next:
            if curr.next.key == key:
                curr.next = curr.next.next
                return 
            curr = curr.next

# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)

# Time Complexity: O(N/K) where N is the number of all possible keys and K is the size of the hashmap. In the worst case, all keys will hash to the same index, resulting in a linked list of length N at that index. Therefore, the time complexity for put, get, and remove operations is O(N/K).
# Space Complexity: O(K + M) where K is the size of the hashmap and M is the number of unique keys inserted into the hashmap. The space complexity is O(K) for the initial array of linked lists and O(M) for the nodes in the linked lists that store the key-value pairs.

# main function

if __name__=="__main__":
    myHashMap = MyHashMap()
    myHashMap.put(1, 1) 
    myHashMap.put(2, 2) 
    print(myHashMap.get(1))            # returns 1
    print(myHashMap.get(3))            # returns -1 (not found)
    myHashMap.put(2, 1)                # update the existing value
    print(myHashMap.get(2))            # returns 1 
    myHashMap.remove(2)                # remove the mapping for 2
    print(myHashMap.get(2))            # returns -1 (not found)
