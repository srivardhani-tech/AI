class WaterJugProblem:
    def __init__(self, jug1_capacity, jug2_capacity, target):
        self.jug1_capacity = jug1_capacity
        self.jug2_capacity = jug2_capacity
        self.target = target
        self.states_visited = set()

    def is_valid_state(self, state):
        jug1, jug2 = state
        return 0 <= jug1 <= self.jug1_capacity and 0 <= jug2 <= self.jug2_capacity

    def is_goal_state(self, state):
        return state[0] == self.target or state[1] == self.target

    def get_successors(self, state):
        successors = []

        # Fill jug1
        successors.append((self.jug1_capacity, state[1]))

        # Fill jug2
        successors.append((state[0], self.jug2_capacity))

        # Empty jug1
        successors.append((0, state[1]))

        # Empty jug2
        successors.append((state[0], 0))

        # Pour from jug1 to jug2
        pour_amount = min(state[0], self.jug2_capacity - state[1])
        successors.append((state[0] - pour_amount, state[1] + pour_amount))

        # Pour from jug2 to jug1
        pour_amount = min(state[1], self.jug1_capacity - state[0])
        successors.append((state[0] + pour_amount, state[1] - pour_amount))

        return [s for s in successors if self.is_valid_state(s)]

    def solve(self):
        initial_state = (0, 0)
        stack = [initial_state]

        while stack:
            current_state = stack.pop()

            if current_state in self.states_visited:
                continue

            self.states_visited.add(current_state)

            if self.is_goal_state(current_state):
                return current_state

            successors = self.get_successors(current_state)
            stack.extend(successors)

        return None


# Example usage for the given problem
jug_problem = WaterJugProblem(jug1_capacity=4, jug2_capacity=3, target=2)
solution = jug_problem.solve()

if solution:
    print("Solution found:", solution)
else:
    print("No solution found.")
