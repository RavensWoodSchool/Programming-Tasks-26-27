"""
TASK: 01 2D Grid Manipulator

# Create an NxM grid resolver - https://bk2coady.medium.com/daily-coding-problem-62-bfe0e398247b
- Initialises a grid filled with zeros
- Allows user to "paint" coordinates
- Displays updated grid each time

TODO:
- Fill in functions
- Add demonstration code under `if __name__ == "__main__":`
"""

def main():
    # TODO: Write demonstration/testing code
    # If you want to delete all the code here and work just with a blank file go ahead, remember anything under the if __name__=="__main__":
    # will only run if this module is being run directly. So used this subprocedure to carry out testing if it is going to be an imported file.
    rows = int(input("Enter number of rows: "))
    cols = int(input("Enter number of columns: "))

    grid = create_grid(rows, cols)

def create_grid(rows, cols):
    grid = []
    for r in range(rows):
        row = []
        for c in range(cols):
            row.append(0)
        grid.append(row)
    return grid

def print_grid(grid):
    for row in grid:
        line = ""
        for val in row:
            line = line + str(val) + " "
        print(line)

def paint_coordinate(grid, r, c, val):
    if r >= 0 and r < len(grid):
        if c >= 0 and c < len(grid[0]):
            grid[r][c] = val
        else:
            print("column is out of range")
    else:
        print("row is out of range")



if __name__ == "__main__":
    main()
