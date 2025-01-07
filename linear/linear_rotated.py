from typing import List

def rotated_list_linear_sol(numbers: List[int])-> int:
    position: int = 0

    while position < len(numbers) - 1:
        if numbers[position] > numbers[position + 1]:
            return position + 1
        position += 1
    if position == len(numbers) -1:
        return 0
    return -1