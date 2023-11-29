import random

def objective_function(x):
    # Replace this with your own objective function to be maximized
    return -(x ** 2)

def hill_climbing(initial_state, max_iterations):
    current_state = initial_state

    for _ in range(max_iterations):
        neighbors = get_neighbors(current_state)
        next_state = max(neighbors, key=objective_function)

        if objective_function(next_state) <= objective_function(current_state):
            break  # Stop if no improvement

        current_state = next_state

    return current_state

def get_neighbors(state):
    # Generate neighboring states by slightly perturbing the current state
    return [state + random.uniform(-0.5, 0.5) for _ in range(3)]

# Example usage:
initial_state = 5.0
max_iterations = 100

result = hill_climbing(initial_state, max_iterations)
print("Optimal state:", result)
print("Objective value:", objective_function(result))
