class MinStack:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []
        self.min_stack = []
    
    def push(self, val:int) -> None:
        """
        Pushes the element val onto the stack.
        
        Parameters:
        val (int): The value to be pushed onto the stack.
        """
        self.stack.append(val)
        minval = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(minval)
        # If min_stack is empty or the new value is smaller or equal to the current minimum, push it onto min_stack
    
    def pop(self) -> None:
        """
        Removes the element on the top of the stack.
        """
        if self.stack:
            self.stack.pop()
            self.min_stack.pop()
    
    def top(self) -> int:

        """
        Gets the top element of the stack.
        
        Returns:
        int: The top element of the stack.
        """
        if self.stack:
            return self.stack[-1]
        return None

    def getMin(self) -> int:
        """
        Retrieves the minimum element in the stack.
        
        Returns:
        int: The minimum element in the stack.
        """
        if self.min_stack:
            return self.min_stack[-1]
        return None
    

if __name__ == "__main__":
    min_stack = MinStack()
    min_stack.push(-2)
    min_stack.push(0)
    min_stack.push(-3)
    print(min_stack.getMin())  # Returns -3
    min_stack.pop()
    print(min_stack.top())      # Returns 0
    print(min_stack.getMin())   # Returns -2