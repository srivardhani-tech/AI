class SlidingPuzzle:
    def __init__(self, initial_state):
        self.state = initial_state
        self.goal_state = [[1, 2, 3], [4, 5, 6], [7, 8, 0]]  # 0 represents the empty space

    def display(self):
        for row in self.state:
            print(row)
        print()

    def find_blank(self):
        for i in range(3):
            for j in range(3):
                if self.state[i][j] == 0:
                    return i, j

    def move(self, direction):
        i, j = self.find_blank()

        if direction == 'up' and i > 0:
            self.state[i][j], self.state[i - 1][j] = self.state[i - 1][j], self.state[i][j]
        elif direction == 'down' and i < 2:
            self.state[i][j], self.state[i + 1][j] = self.state[i + 1][j], self.state[i][j]
        elif direction == 'left' and j > 0:
            self.state[i][j], self.state[i][j - 1] = self.state[i][j - 1], self.state[i][j]
        elif direction == 'right' and j < 2:
            self.state[i][j], self.state[i][j + 1] = self.state[i][j + 1], self.state[i][j]
        else:
            print("Invalid move")

    def is_solved(self):
        return self.state == self.goal_state


# Example usage:
initial_state = [[1, 2, 3], [4, 0, 6], [7, 5, 8]]  # You can change the initial state
puzzle = SlidingPuzzle(initial_state)

print("Initial state:")
puzzle.display()

while not puzzle.is_solved():
    direction = input("Enter move (up/down/left/right): ")
    puzzle.move(direction)
    puzzle.display()

print("Puzzle solved!")
