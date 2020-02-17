"""
Search a sorted array for first occurrence of k

Write a method that takes a sorted array and a key and returns the index of the first occurence
of that key in the array. Return -1 if the key does not appear in the array.
"""

import math

test_array = [-13, -1, 0, 4, 21, 52, 52, 52, 52, 52, 73, 74, 101]

# my solution, is not optimal in time O(logn)
def first_occurrence_search(x: int, A: list) -> int:
    index = -1
    offset = 0
    while(len(A)>0):
        search_index = math.floor(len(A)/2)
        currVal = A[search_index]
        if x == currVal:
            index = search_index
            break
        elif x < currVal:
            A = A[0:search_index]
        else:
            offset += search_index
            A = A[search_index:len(A)]
    return index + offset

# Brute force solution, is complete and optimal in O(n)
def brute_force(x: int, A: list) -> int:
    for i in range(len(A)):
        if A[i] == x:
            return i

# my solution, nearly optimal in time O(logn)
def first_occurrence_search_take_two(x: int, A: list) -> int:
    index = -1
    offset = 0
    while(len(A)!=1):
        search_index = math.floor(len(A)/2)
        currVal = A[search_index]
        if x == currVal:
            index = search_index
            A = A[0:search_index]
        elif x < currVal:
            A = A[0:search_index]
        else:
            offset += search_index
            A = A[search_index:len(A)]
    return index + offset

# Book solution: O(logn), is optimal
def optimal_first_occurence(x: int, A: list) -> int:
    left, right, result = 0, len(A) - 1, -1
    while left <= right:
        mid = (left + right) // 2
        if A[mid] > x:
            right = mid - 1
        elif A[mid] == x:
            result = mid
            right = mid - 1
        else:
            left = mid + 1
    return result

print(brute_force(4, test_array))
for x in test_array:    
    print(first_occurrence_search(x, test_array))

for x in test_array:
    print(optimal_first_occurence(x, test_array))

for x in test_array:
    print(first_occurrence_search_take_two(x, test_array))