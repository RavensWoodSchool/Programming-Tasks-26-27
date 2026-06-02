"""
TASK: 03 Insertion Sort

# Insertion Sort Tester
Generate an unsorted list (maybe use RNG). Implement:
- Insertion sort without using inbuild sorts
- Count number of comparions
Then benchmark them with random inputs.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
import random
import time 

total_comparisons = 0
tests = 100

start = time.time()

for _ in range(tests):
    numbers = [random.randint(1, 1000) for _ in range(100)]
    comparison = 0
    for i in range(1, len(numbers)):
        key = numbers[i]
        j = j - 1
    

