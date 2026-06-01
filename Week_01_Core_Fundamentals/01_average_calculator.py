"""
TASK: 01 Average Calculator

# Average Calculator
Write a Python program that:
- Prompts the user for a list of numbers.
- Stores them in a 1D list.
- Calculates the mean *without using built-in statistics libraries*.
- Includes input validation.
- Implements a reusable function: `calculate_average(values)`.

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""
def calculate_average(values):
    total = sum(values)
    return total / len(values)

while True:
    n = int(input("How many numbers?"))
    if n <= 0:
        print("Please enter a number greater than  0")
    else:
        break
numbers = []:
    while True:
        num = input("Enter a number: ")
        numbers.append(num)
        break
average = calculate_average(numbers)
                     
