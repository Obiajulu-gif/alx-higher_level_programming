#!/usr/bin/python3
''' N queens problem '''
import sys


class NQueensSolver:
    ''' class to solve the N queens problem '''
    def __init__(self, N):
        self.N = N
        self.board = [[0 for _ in range(N)] for _ in range(N)]

    def is_safe(self, row, col):
        ''' check if a queen can be placed on board[row][col] '''
        for i in range(col):
            if self.board[row][i] == 1:
                return False

        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        for i, j in zip(range(row, self.N, 1), range(col, -1, -1)):
            if self.board[i][j] == 1:
                return False

        return True

    def solve_n_queens(self, col):
        ''' solve the N queens problem '''
        if col >= self.N:
            self.print_solution()
            return True

        res = False
        for i in range(self.N):
            if self.is_safe(i, col):
                self.board[i][col] = 1
                res = self.solve_n_queens(col + 1) or res
                self.board[i][col] = 0

        return res

    def print_solution(self):
        ''' print the solution '''
        queens = []
        for i in range(self.N):
            for j in range(self.N):
                if self.board[i][j] == 1:
                    queens.append([i, j])
        print(queens)

    def solve(self):
        ''' solve the N queens problem '''
        if self.N < 4:
            print("N must be at least 4")
            sys.exit(1)

        self.solve_n_queens(0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    try:
        N = int(sys.argv[1])
        solver = NQueensSolver(N)
        solver.solve()
    except ValueError:
        print("N must be a number")
        sys.exit(1)
