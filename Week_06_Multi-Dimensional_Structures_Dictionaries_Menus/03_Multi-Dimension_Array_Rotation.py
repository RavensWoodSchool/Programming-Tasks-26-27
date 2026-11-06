"""
TASK: 03 Multi-Dimension Array Rotation

# Rotate a 2D matrix 90 degrees clockwise manually
Good luck

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    matrix = [[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]]

    print_matrix(matrix)

    rotated = rotate(matrix)

    print_matrix(rotated)

def print_matrix(matrix):
    for row in matrix:
        print(row)

def rotate(matrix):
    rows = len(matrix)
    cols = len(matrix[0])

    rotated = []
    for i in range(cols):
        newRow = []
        for j in range(rows):
            newRow.append(0)
        rotated.append(newRow)

    for i in range(rows):
        for j in range(cols):
            rotated[j][rows - 1 - i] = matrix[i][j]

    return rotated

if __name__ == "__main__":
    main()
