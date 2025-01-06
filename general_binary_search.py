from typing import List
def general_binary_search(numbers: List[int], low: int, high: int, condition)-> int:
   
    while low <= high:
        middle_index: int = (low + high) // 2
        middle_number: int = numbers[middle_index]

        result = condition(middle_number)

        if result == 'found':
            return middle_index + 1
        elif result == 'left':
            high = middle_index - 1
        else:
            low = middle_index + 1
    return -1

