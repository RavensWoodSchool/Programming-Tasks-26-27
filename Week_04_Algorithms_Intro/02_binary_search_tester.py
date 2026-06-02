"""
TASK: 02 Binary Search Tester

# Binary Search Tester
Generate a sorted list. Implement:
- iterative binary search
- recursive binary search
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random
import time

numbers = list(range(1, 10001))

def iterative_binary_search(aee, target):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) //2
        if arr[mid] == target:
            low = mid + 1
        elif arr[mid] < target:
            high = mid - 1

return -1
