"""
TASK: 01 Bubble Sort

# Bubble Sort
Implement Bubble Sort on any size list:
- Do not use built-in sort()
- Count swaps
- Extend by

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
numbers = input("Enter number seperated by spaces: ").split()

for i in range(len(numbers)):
    numbers[i] = int(numbers[i])

swaps = 0

for i in range(len(numbers)):
    for j in range(len(numbers) -1):
        if numbers[j[ > numbers[j + 1]
        numbers[j], numbers[j + 1} = numbers[j + 1], numbers[j]
        swaps += 1

print("Sorted list:", numbers)
print("Number of swaps:", swaps)
    

