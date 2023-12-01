import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def a_star_search(graph, start, goal):
    def heuristic(node):
        # Example heuristic: straight-line distance from the node to the goal
        return abs(node[0] - goal[0]) + abs(node[1] - goal[1])

    visited = set()
    priority_queue = [(0 + heuristic(start), 0, start)]  # (f, g, node)

    while priority_queue:
        (f, g, current_node) = heapq.heappop(priority_queue)

        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)

            if current_node == goal:
                print("\nGoal reached!")
                return True

            for neighbor, edge_cost in graph.graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (g + edge_cost + heuristic(neighbor), g + edge_cost, neighbor))

    print("\nGoal not reached.")
    return False

# Example usage:
graph = Graph()
graph.add_edge((0, 0), [((0, 1), 1), ((1, 0), 1)])
graph.add_edge((0, 1), [((0, 0), 1), ((0, 2), 1), ((1, 1), 1)])
graph.add_edge((0, 2), [((0, 1), 1), ((1, 2), 1)])
graph.add_edge((1, 0), [((0, 0), 1), ((1, 1), 1), ((2, 0), 1)])
graph.add_edge((1, 1), [((0, 1), 1), ((1, 0), 1), ((1, 2), 1), ((2, 1), 1)])
graph.add_edge((1, 2), [((0, 2), 1), ((1, 1), 1), ((2, 2), 1)])
graph.add_edge((2, 0), [((1, 0), 1), ((2, 1), 1)])
graph.add_edge((2, 1), [((1, 1), 1), ((2, 0), 1), ((2, 2), 1)])
graph.add_edge((2, 2), [((1, 2), 1), ((2, 1), 1)])

start_node = (0, 0)
goal_node = (2, 2)

print("A* Search:")
a_star_search(graph, start_node, goal_node)
