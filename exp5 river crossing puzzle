class State:
    def __init__(self, missionaries_left, cannibals_left, boat_left, missionaries_right, cannibals_right):
        self.missionaries_left = missionaries_left
        self.cannibals_left = cannibals_left
        self.boat_left = boat_left
        self.missionaries_right = missionaries_right
        self.cannibals_right = cannibals_right

    def is_valid(self):
        # Check if the state is valid according to the given constraints
        if (
            self.missionaries_left < 0
            or self.cannibals_left < 0
            or self.missionaries_right < 0
            or self.cannibals_right < 0
            or (
                self.missionaries_left < self.cannibals_left
                and self.missionaries_left > 0
            )
            or (
                self.missionaries_right < self.cannibals_right
                and self.missionaries_right > 0
            )
        ):
            return False
        return True

    def is_goal(self):
        # Check if the state is the goal state
        return self.missionaries_left == 0 and self.cannibals_left == 0

    def __eq__(self, other):
        return (
            self.missionaries_left == other.missionaries_left
            and self.cannibals_left == other.cannibals_left
            and self.boat_left == other.boat_left
            and self.missionaries_right == other.missionaries_right
            and self.cannibals_right == other.cannibals_right
        )

    def __hash__(self):
        return hash(
            (
                self.missionaries_left,
                self.cannibals_left,
                self.boat_left,
                self.missionaries_right,
                self.cannibals_right,
            )
        )


def print_move(state1, state2):
    # Print the move from state1 to state2
    if state1.boat_left > state2.boat_left:
        boat_side = "right"
    else:
        boat_side = "left"

    missionaries_moved = abs(state1.missionaries_left - state2.missionaries_left)
    cannibals_moved = abs(state1.cannibals_left - state2.cannibals_left)

    print(
        f"Move {missionaries_moved} missionaries and {cannibals_moved} cannibals from {boat_side} to {state2.boat_left} side."
    )


def successors(current_state):
    # Generate successor states from the current state
    possible_moves = [
        (1, 0),
        (2, 0),
        (0, 1),
        (0, 2),
        (1, 1),
    ]

    boat_side = current_state.boat_left
    if current_state.boat_left == 0:
        boat_side = 1

    next_states = []
    for move in possible_moves:
        new_state = State(
            current_state.missionaries_left - move[0],
            current_state.cannibals_left - move[1],
            1 - current_state.boat_left,
            current_state.missionaries_right + move[0],
            current_state.cannibals_right + move[1],
        )

        if new_state.is_valid():
            next_states.append(new_state)

    return next_states


def depth_first_search(initial_state):
    stack = [initial_state]
    visited = set()

    while stack:
        current_state = stack.pop()

        if current_state.is_goal():
            return True

        if current_state not in visited:
            visited.add(current_state)

            next_states = successors(current_state)
            for next_state in next_states:
                stack.append(next_state)
                print_move(current_state, next_state)

    return False


# Example usage:
initial_state = State(3, 3, 1, 0, 0)
result = depth_first_search(initial_state)

if result:
    print("Solution found!")
else:
    print("No solution found.")
