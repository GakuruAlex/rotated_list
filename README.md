# Rotated List #

Given a list of numbers obtained by rotating a sorted list in ascending order,determine the minimum number of times the original list was rotated to obtain the current list.Rotating a list is defined as removing the last element of the list and adding it before the first element in the list.

## Problem Statement ##

Find the minimum number of times a list sorted in ascending order is rotated to obtain current version of list.

## Input ##

Numbers: A rotated listed i.e [9,10,11,5,6,7,8]

## Output ##

Rotation: Number of times original list was rotated to get current list i.e 3 for list above.

## Test Cases ##

### Possible cases ###

1. An empty list.

2. A listed sorted 3 times i.e [12, 13, 15, 0, 3, 5, 7]

3. A list rotated n times i.e [0, 3, 5, 7, 12, 13, 15] where n is the size of the list

4. A list rotated 1 i.e [15, 3, 5, 7, 8, 11]

5. A list rotated 0 times i.e [14, 16, 17, 19, 21]

6. A list with one element i.e [4]

7. A list with negative integers rotated 4 times i.e [-5, -4, -3, -1, -7, -9, -10]

8. A list with negative and positive integers rotated 5 times i.e  [-12,-10, 0, 4, 6, -24, -20, -18, -14]

9. A rotated list with repeated numbers [16, 19, 19, 20, 20, 0, 4, 4, 6, 6, 8, 10]

### Tests ###

tests =[
    
            {
                "input":[],
                "output":-1
            },

            {
                "input": [12, 13, 15, 0, 3, 5, 7],
                "output": 3
            },

            {
                "input": [4],
                "output": 0
            },

            {
                "input": [0, 3, 5, 7, 12, 13, 15],
                "output": 0
            },

            {
                "input": [15, 3, 5, 7, 8, 11],
                "output": 1
            },

            {
                "input": [-5, -4, -3, -1, -7, -9, -10],
                "output": 4
            },

            {
                "input": [12, 14, 16, 18, 0, 1, 2, 3, 4, 6, 7, 8, 9, 10],
                "output": 4
            }
    
]
