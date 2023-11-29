class VacuumCleaner:
    def __init__(self, grid):
        self.grid = grid
        self.rows = len(grid)
        self.cols = len(grid[0])
        self.position = (0, 0)  # Starting position of the cleaner

    def display_grid(self):
        for row in self.grid:
            print(row)
        print()

    def move_up(self):
        if self.position[0] > 0:
            self.position = (self.position[0] - 1, self.position[1])

    def move_down(self):
        if self.position[0] < self.rows - 1:
            self.position = (self.position[0] + 1, self.position[1])

    def move_left(self):
        if self.position[1] > 0:
            self.position = (self.position[0], self.position[1] - 1)

    def move_right(self):
        if self.position[1] < self.cols - 1:
            self.position = (self.position[0], self.position[1] + 1)

    def clean(self):
        while any(1 in row for row in self.grid):
            self.display_grid()
            dirty_cells = [(i, j) for i in range(self.rows) for j in range(self.cols) if self.grid[i][j] == 1]

            if not dirty_cells:
                print("Cleaning complete!")
                break

            nearest_dirty_cell = min(dirty_cells, key=lambda cell: abs(cell[0] - self.position[0]) + abs(cell[1] - self.position[1]))

            if nearest_dirty_cell[0] < self.position[0]:
                self.move_up()
            elif nearest_dirty_cell[0] > self.position[0]:
                self.move_down()
            elif nearest_dirty_cell[1] < self.position[1]:
                self.move_left()
            elif nearest_dirty_cell[1] > self.position[1]:
                self.move_right()

            i, j = self.position
            print(f"Cleaning cell ({i}, {j})")
            self.grid[i][j] = 0  # Mark the cell as clean

# Example usage:
grid = [
    [1, 0, 1, 1],
    [0, 1, 0, 1],
    [1, 1, 1, 0],
    [0, 0, 1, 0]
]

vacuum_cleaner = VacuumCleaner(grid)
vacuum_cleaner.clean()
