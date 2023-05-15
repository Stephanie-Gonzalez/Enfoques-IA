# -*- coding: utf-8 -*-
"""

@author: sttep
"""

from queue import Queue

# Función para representar el estado del rompecabezas
class PuzzleState:
    def __init__(self, board):
        self.board = board

    def __eq__(self, other):
        return self.board == other.board

    def __hash__(self):
        return hash(str(self.board))

    def __str__(self):
        return '\n'.join([str(row) for row in self.board])

    def find_blank_position(self):
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == 0:
                    return i, j

    def generate_successors(self):
        successors = []
        i, j = self.find_blank_position()

        # Movimiento hacia arriba
        if i > 0:
            new_board = [list(row) for row in self.board]
            new_board[i][j], new_board[i - 1][j] = new_board[i - 1][j], new_board[i][j]
            successors.append(PuzzleState(new_board))

        # Movimiento hacia abajo
        if i < 2:
            new_board = [list(row) for row in self.board]
            new_board[i][j], new_board[i + 1][j] = new_board[i + 1][j], new_board[i][j]
            successors.append(PuzzleState(new_board))

        # Movimiento hacia la izquierda
        if j > 0:
            new_board = [list(row) for row in self.board]
            new_board[i][j], new_board[i][j - 1] = new_board[i][j - 1], new_board[i][j]
            successors.append(PuzzleState(new_board))

        # Movimiento hacia la derecha
        if j < 2:
            new_board = [list(row) for row in self.board]
            new_board[i][j], new_board[i][j + 1] = new_board[i][j + 1], new_board[i][j]
            successors.append(PuzzleState(new_board))

        return successors

# Función de búsqueda en anchura para resolver el rompecabezas
def bfs_puzzle_solver(initial_state, goal_state):
    visited = set()
    queue = Queue()
    queue.put((initial_state, []))

    while not queue.empty():
        state, path = queue.get()

        if state == goal_state:
            return path

        if state not in visited:
            visited.add(state)
            successors = state.generate_successors()
            for successor in successors:
                queue.put((successor, path + [successor]))

    return None  # No se encontró una solución

# Ejemplo de uso
initial_state = PuzzleState([[2, 8, 3], [1, 6, 4], [7, 0, 5]])
goal_state = PuzzleState([[1, 2, 3], [8, 0, 4], [7, 6, 5]])

path = bfs_puzzle_solver(initial_state, goal_state)
if path:
    print("Se encontró una solución:")
    for state in path:
        print(state)
        print()
else:
    print("No se encontró una solución.")