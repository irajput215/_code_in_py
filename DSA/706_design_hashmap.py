class ListNode:
    def __init__(self, key,val):
        self.key = key
        self.val = val
        self.next = None

class MyHashMap:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hmap = [ListNode(-1,-1) for _ in range(10**4)]
    
    def put(self, key: int, value: int) -> None:
        
        index = key % (len(self.hmap))
        cur = self.hmap[index]

        while cur.next:
            if cur.next.key==key:
                cur.next.val = value
                return
            cur = cur.next
        cur.next = ListNode(key, value)
    
    def get(self, key: int) -> int:
        index = key % (len(self.hmap))
        cur = self.hmap[index]

        while cur.next:
            if cur.next.key == key:
                return cur.next.val
            cur = cur.next
        return -1
    
    def remove(self, key: int) -> None:
        index = key % (len(self.hmap))
        cur = self.hmap[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return 
            cur = cur.next

if __name__ == "__main__":
    my_hash_map = MyHashMap()
    my_hash_map.put(1, 1)          # The map is now [[1,1]]
    my_hash_map.put(2, 2)          # The map is now [[1,1], [2,2]]
    print(my_hash_map.get(1))      # Returns 1
    print(my_hash_map.get(3))      # Returns -1 (not found)
    my_hash_map.put(2, 69)          # Update the existing value
    print(my_hash_map.get(2))      # Returns 1 
    my_hash_map.remove(2)          # Remove the mapping for 2
    print(my_hash_map.get(2))      # Returns -1 (not found)
