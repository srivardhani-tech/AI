import heapq

class Graph:
    def __init__(self):
        self.graph = {}

    def add_edge(self, node, neighbors):
        self.graph[node] = neighbors

def best_first_search(graph, start, goal):
    visited = set()
    priority_queue = [(0, start)]
    
    while priority_queue:
        (cost, current_node) = heapq.heappop(priority_queue)
        
        if current_node not in visited:
            print(current_node, end=" ")
            visited.add(current_node)

            if current_node == goal:
                print("\nGoal reached!")
                return True

            for neighbor, edge_cost in graph.graph[current_node]:
                if neighbor not in visited:
                    heapq.heappush(priority_queue, (edge_cost, neighbor))

    print("\nGoal not reached.")
    return False

# Example usage:
graph = Graph()
graph.add_edge('A', [('B', 5), ('C', 2)])
graph.add_edge('B', [('D', 3), ('E', 8)])
graph.add_edge('C', [('F', 1)])
graph.add_edge('D', [])
graph.add_edge('E', [('G', 2)])
graph.add_edge('F', [])
graph.add_edge('G', [])

start_node = 'A'
goal_node = 'G'

print("Best-First Search:")
best_first_search(graph, start_node, goal_node)
