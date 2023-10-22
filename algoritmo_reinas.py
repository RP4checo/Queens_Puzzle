def solve_n_queens(n):
    def is_safe(board, row, col):
        # Verifica si es seguro colocar una reina en la posición (row, col)
        for i in range(col):
            if board[row][i] == 1:
                return False
        for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        for i, j in zip(range(row, n, 1), range(col, -1, -1)):
            if board[i][j] == 1:
                return False
        return True

    def solve(board, col, count):
        if col >= n:
            # Todas las reinas están colocadas, imprime el tablero con número
            print(f"Tablero {count}:")
            print("")
            print_board(board)
            print("")
            return count + 1

        for i in range(n):
            if is_safe(board, i, col):
                board[i][col] = 1
                count = solve(board, col + 1, count)
                board[i][col] = 0

        return count

    def print_board(board):
        for i in range(n):
            for j in range(n):
                print(board[i][j], end=" ")
            print()

    board = [[0] * n for _ in range(n)]

    solutions_count = solve(board, 0, 1)

    if solutions_count == 1:
        print("No hay más soluciones para el problema de las 8 reinas.")
    else:
        print(f"Se encontraron un total de {solutions_count - 1} soluciones al problema de las 8 reinas.")

# Llamada a la función para resolver el problema con 8 reinas
solve_n_queens(8)