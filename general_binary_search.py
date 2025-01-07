from typing import List
def general_binary_search(low: int, high: int, condition)-> int:
   
    while low <= high:
        middle_index: int = (low + high) // 2
        
        result = condition(middle_index)
        print(f"Middle index: {middle_index} low {low} high {high}")
        if result == 'found':
            return middle_index + 1
        elif result == 'left':
            high = middle_index - 1
        elif result == 'right':
            low = middle_index + 1
        elif result == 'no rotation':
            return 0
    return -1

