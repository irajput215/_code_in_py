class ListNode:
    def __init__(self,key):
        self.key = key
        self.next = None

class MyHashSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.set = [ListNode(0) for _ in range(10**4)]
    
    def add(self,key:int)->None:
        """
        Inserts the value key into the HashSet.
        
        Parameters:
        key (int): The value to be added to the HashSet.
        """
        index = key % (len(self.set))
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return
            cur = cur.next
        cur.next = ListNode(key)
    
    def remove(self,key:int)->None:
        """
        Removes the value key from the HashSet.
        
        Parameters:
        key (int): The value to be removed from the HashSet.
        """
        index = key % (len(self.set))
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                cur.next = cur.next.next
                return
            cur = cur.next
    
    def contains(self,key:int)->bool:
        """
        Returns true if this set contains the specified element key.
        
        Parameters:
        key (int): The value to be checked in the HashSet.
        
        Returns:
        bool: True if the HashSet contains the key, False otherwise.
        """
        index = key % (len(self.set))
        cur = self.set[index]

        while cur.next:
            if cur.next.key == key:
                return True
            cur = cur.next
        return False
    

if __name__ == "__main__":
    hashset = MyHashSet()
    hashset.add(1)
    hashset.add(2)
    print(hashset.contains(1)) # returns True
    print(hashset.contains(3)) # returns False
    hashset.add(2)
    print(hashset.contains(2)) # returns True
    hashset.remove(2)
    print(hashset.contains(2)) # returns False