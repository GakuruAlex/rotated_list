from typing import List
from general_binary_search import general_binary_search

def rotated_list_binary_sol(numbers: List[int]) -> int:
    if len(numbers) < 1:
        return -1
    def condition(middle_index: int):
        middle_number: int = numbers[middle_index]
        if middle_number > numbers[middle_index + 1]:
            return 'found'
        elif middle_number < numbers[middle_index + 1] and middle_number < numbers[-1]:
            return 'left'
        elif middle_number < numbers[middle_index + 1] and middle_number > numbers[-1]:
            return 'right'
    return general_binary_search(0, len(numbers)-2, condition)

def main()->None:
    print(rotated_list_binary_sol([-20, -15, -10, 0, 5, 15, 20]))


if __name__ =="__main__":
    main()