
def nearest_greater_to_right(heights):
    """
    Finds the nearest greater element to the right for each element in the heights list.

    Parameters:
    heights (list): A list of integers representing heights.

    Returns:
    list: A list containing the nearest greater element to the right for each element in heights.
          If there is no greater element to the right, -1 is placed in that position.
    """
    n = len(heights)
    stack = []
    ngr = []

    for i in range(len(heights)-1,-1,-1):
        
        while stack and stack[-1]<=heights[i]:
            stack.pop()
        if not stack:
            ngr.append(-1)
        else:
            ngr.append(stack[-1])
        stack.append(heights[i])
    ngr.reverse()
    return ngr

def nearest_smallest_to_left(heights):
    """
    Finds the nearest smaller element to the left for each element in the heights list.

    Parameters:
    heights (list): A list of integers representing heights.

    Returns:
    list: A list containing the nearest smaller element to the left for each element in heights.
          If there is no smaller element to the left, -1 is placed in that position.
    """
    n = len(heights)
    stack = []
    nsl = []

    for i in range(len(heights)):
        
        while stack and stack[-1]>=heights[i]:
            stack.pop()
        if not stack:
            nsl.append(-1)
        else:
            nsl.append(stack[-1])
        stack.append(heights[i])
    
    return nsl

def nearest_greater_to_left(heights):
    """
    Finds the nearest greater element to the left for each element in the heights list.

    Parameters:
    heights (list): A list of integers representing heights.

    Returns:
    list: A list containing the nearest greater element to the left for each element in heights.
          If there is no greater element to the left, -1 is placed in that position.
    """
    n = len(heights)
    stack = []
    ngl = []

    for i in range(len(heights)):
        
        while stack and stack[-1]<=heights[i]:
            stack.pop()
        if not stack:
            ngl.append(-1)
        else:
            ngl.append(stack[-1])
        stack.append(heights[i])
    
    return ngl

def nearest_smallest_to_right(heights):
    """
    Finds the nearest smaller element to the right for each element in the heights list.

    Parameters:
    heights (list): A list of integers representing heights.

    Returns:
    list: A list containing the nearest smaller element to the right for each element in heights.
          If there is no smaller element to the right, -1 is placed in that position.
    """
    n = len(heights)
    stack = []
    nsr = []

    for i in range(len(heights)-1,-1,-1):
        
        while stack and stack[-1]>=heights[i]:
            stack.pop()
        if not stack:
            nsr.append(-1)
        else:
            nsr.append(stack[-1])
        stack.append(heights[i])
    nsr.reverse()
    return nsr

# Example usage:
if __name__ == "__main__":
    heights = [4, 5, 2, 10, 8]
    result = nearest_greater_to_right(heights)
    print("Heights:", heights)
    print("Nearest Greater to Right:", result)

    result_left = nearest_greater_to_left(heights)
    print("Nearest Greater to Left:", result_left)
    result_nsr = nearest_smallest_to_right(heights)
    print("Nearest Smallest to Right:", result_nsr)
    result_nsl = nearest_smallest_to_left(heights)
    print("Nearest Smallest to Left:", result_nsl)
    
    """
    Output:
    Heights: [4, 5, 2, 10, 8]
    Nearest Greater to Right: [5, 10, 10, -1, -1]
    """
    