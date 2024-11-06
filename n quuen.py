def print_solution(board, n):
    for row in board:
        print(" ".join("Q" if cell else "." for cell in row))
    print()

def is_safe(row, col, columns, left_diagonal, right_diagonal, n):
    # Check if placing a queen here conflicts with any existing queens
    if columns[col] or left_diagonal[row - col + n - 1] or right_diagonal[row + col]:
        return False
    return True

def solve_n_queens(board, row, columns, left_diagonal, right_diagonal, n, solutions):
    # If we've placed queens in all rows, add the solution
    if row == n:
        solutions.append([row[:] for row in board])
        return True
    
    solution_found = False
    for col in range(n):
        if is_safe(row, col, columns, left_diagonal, right_diagonal, n):
            # Place the queen
            board[row][col] = 1
            columns[col] = True
            left_diagonal[row - col + n - 1] = True
            right_diagonal[row + col] = True

            # Recur to place queens in the next row
            solution_found = solve_n_queens(board, row + 1, columns, left_diagonal, right_diagonal, n, solutions) or solution_found

            # Backtrack: remove the queen and reset constraints
            board[row][col] = 0
            columns[col] = False
            left_diagonal[row - col + n - 1] = False
            right_diagonal[row + col] = False

    return solution_found

def n_queens(n):
    # Initialize the board and tracking arrays
    board = [[0] * n for _ in range(n)]
    columns = [False] * n
    left_diagonal = [False] * (2 * n - 1)
    right_diagonal = [False] * (2 * n - 1)
    solutions = []

    # Start solving
    solve_n_queens(board, 0, columns, left_diagonal, right_diagonal, n, solutions)

    # Output all solutions
    print(f"Total solutions for {n}-Queens problem: {len(solutions)}\n")
    for index, solution in enumerate(solutions, start=1):
        print(f"Solution {index}:")
        print_solution(solution, n)

# Input
n = int(input("Enter the number of queens: "))
n_queens(n)
