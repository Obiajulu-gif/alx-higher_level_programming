#!/usr/bin/python3
import sys


def is_safe(board, row, col, N):
    ''' check if a queen can be placed on board[row][col] '''
    for i in range(col):
        if board[row][i] == 1:
            return False

    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        ''' check upper diagonal on left side '''
        if board[i][j] == 1:
            return False

    for i, j in zip(range(row, N, 1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False
    return True


def solve_n_queens(board, col, N):
    ''' solve n queens '''
    if col >= N:
        print_solution(board, N)
        return True

    res = False
    for i in range(N):
        if is_safe(board, i, col, N):
            board[i][col] = 1
            res = solve_n_queens(board, col + 1, N) or res
            board[i][col] = 0
    return res


def print_solution(board, N):
    ''' print the solution '''
    queens = []
    for i in range(N):
        for j in range(N):
            if board[i][j] == 1:
                queens.append([i, j])
    print(queens)


def nqueens(N):
    ''' n queens '''
    if not isinstance(N, int):
        print("N must be a number")
        sys.exit(1)

    if N < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(N)] for _ in range(N)]
    solve_n_queens(board, 0, N)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        nqueens(N)
    except ValueError:
        print("N must be a number")
        sys.exit(1)
